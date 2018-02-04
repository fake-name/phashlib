"""
Copyright (c) 2013-2016, Johannes Buchner
Copyright (c) 2016, Connor Wolf
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

    Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.
"""


# code from imagehash https://github.com/JohannesBuchner/imagehash
import io
import hashlib
import numpy
import scipy.fftpack
from PIL import Image

def binary_array_to_hex(arr):
	h = 0
	s = []
	for i,v in enumerate(arr.flatten()):
		if v:
			h += 2**(i % 8)
		if (i % 8) == 7:
			s.append(hex(h)[2:].rjust(2, '0'))
			h = 0
	return "".join(s)




def binStrToInt(inStr):
	if len(inStr) != 64:
		raise ValueError("Input strings must be 64 chars long!")
	ret = 0
	mask = 1 << len(inStr) - 1
	for char in inStr:  # Specify memory order, so we're (theoretically) platform agnostic
		if char == '1':
			ret |= mask
		mask >>= 1

	# Convert to signed representation
	VALSIZE = 64
	if ret >= 2**(VALSIZE-1):
		ret = ret - 2**VALSIZE
	return ret


def binary_array_to_int(arr):
	ret = 0
	arr = arr.flatten()
	arr = arr[::-1]
	for i,v in enumerate(arr):
		if v:
			ret += 1 << i

	VALSIZE = 64
	if ret >= 2**(VALSIZE-1):
		ret = ret - 2**VALSIZE

	return ret


class ImageHash(object):
	"""
	Hash encapsulation. Can be used for dictionary keys and comparisons.
	"""
	def __init__(self, binary_array):
		self.hash = binary_array

	def __str__(self):
		return binary_array_to_hex(self.hash)

	def __repr__(self):
		return repr(self.hash)

	def __sub__(self, other):
		assert self.hash.shape == other.hash.shape, ('ImageHashes must be of the same shape!', self.hash.shape, other.hash.shape)
		return (self.hash != other.hash).sum()

	def __eq__(self, other):
		return numpy.array_equal(self.hash, other.hash)

	def __ne__(self, other):
		return not numpy.array_equal(self.hash, other.hash)

	def __hash__(self):
		return binary_array_to_int(self.hash)

	def __iter__(self):
		return numpy.nditer(self.hash, order='C')  # Specify memory order, so we're (theoretically) platform agnostic

	def __len__(self):
		return self.hash.size

	def __int__(self):
		ret = 0
		mask = 1 << len(self) - 1
		for bit in numpy.nditer(self.hash, order='C'):  # Specify memory order, so we're (theoretically) platform agnostic
			if bit:
				ret |= mask
			mask >>= 1

		# Convert to signed representation
		VALSIZE = 64
		if ret >= 2**(VALSIZE-1):
			ret = ret - 2**VALSIZE
		return ret



"""
Perceptual Hash computation.

Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

@image must be a PIL instance.
"""
def phash(image, hash_size=32):
	image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)
	pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((hash_size, hash_size))
	dct = scipy.fftpack.dct(pixels)
	dctlowfreq = dct[:8, 1:9]
	avg = dctlowfreq.mean()
	diff = dctlowfreq > avg
	return ImageHash(diff), image

"""
Difference Hash computation.

following http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html

@image must be a PIL instance.
"""
# def dhash(image, hash_size=8):
# 	image = image.convert("L").resize((hash_size + 1, hash_size), Image.ANTIALIAS)
# 	pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((hash_size + 1, hash_size))
# 	# compute differences
# 	diff = pixels[1:,:] > pixels[:-1,:]
# 	return ImageHash(diff)



__dir__ = [phash, ImageHash]

IMAGE_EXTS = ("bmp", "eps", "gif", "im", "jpeg", "jpg", "msp", "pcx", "png", "ppm", "spider", "tiff", "webp", "xbm")

'''
Generate various hashes of file

basepath/fname are required for determining if the passed file is probably an image (by looking at extensions)
Actual file contents must be in fContents

'''
def hashFile(basePath, fname, fContents, shouldPhash=True):
	# basePath, fname, fContents = arg

	fMD5 = hashlib.md5()
	fMD5.update(fContents)
	hexHash = fMD5.hexdigest()

	pHash = None
	# dHash = None

	imX = None
	imY = None

	if (fname.lower().endswith(IMAGE_EXTS) or (basePath.lower().endswith(IMAGE_EXTS) and fname == "")) and shouldPhash:


		im = Image.open(io.BytesIO(fContents))


		# The later calls permute the image size, so we need to save it now
		imX, imY = im.size

		pHashArr, im = phash(im)
		# dHashArr     = dhash(im)

		pHash = int(pHashArr)
		# dHash = int(dHashArr)


	return fname, hexHash, pHash, imX, imY

def getHashDict(fName, fContents):
	dummy_fname, hexHash, pHash, imX, imY = hashFile('', fName, fContents)
	retD = {'hexHash' : hexHash, 'pHash' : pHash, 'imX' : imX, 'imY' : imY}
	return retD


def getMd5Hash(fContents):
	fMD5 = hashlib.md5()
	fMD5.update(fContents)
	hexHash = fMD5.hexdigest()
	return hexHash
