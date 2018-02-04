
import unittest
import phashlib
import os.path

# Unit testing driven by lolcat images
# AS GOD INTENDED!

class TestSequenceFunctions(unittest.TestCase):

	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)


	def test_hashImage1(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		imPath = os.path.join(cwd, 'testimages', 'dangerous-to-go-alone.jpg')

		with open(imPath, "rb") as fp:
			fCont = fp.read()

		basePath, intName = "LOL", "WAT.jpg"
		fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

		self.assertEqual(intName, fname)

		self.assertEqual(hexHash, "dcd6097eeac911efed3124374f44085b" )
		self.assertEqual(pHash,   -149413575039568585 )
		self.assertEqual(imX,     325 )
		self.assertEqual(imY,     307)


	def test_hashImage2(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		imPath = os.path.join(cwd, 'testimages', 'Lolcat_this_is_mah_job.jpg')

		with open(imPath, "rb") as fp:
			fCont = fp.read()

		basePath, intName = "LOL", "WAT.jpg"
		fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

		self.assertEqual(intName, fname)

		self.assertEqual(hexHash, "d9ceeb6b43c2d7d096532eabfa6cf482" )
		self.assertEqual(pHash,   27427800275512429 )
		self.assertEqual(imX,     493 )
		self.assertEqual(imY,     389)


	# check that phash is invariant across format changes
	def test_hashImage2_b(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		imPath = os.path.join(cwd, 'testimages', 'Lolcat_this_is_mah_job.png')

		with open(imPath, "rb") as fp:
			fCont = fp.read()

		basePath, intName = "LOL", "WAT.jpg"
		fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

		self.assertEqual(intName, fname)

		self.assertEqual(hexHash, "1268e704908cc39299d73d6caafc23a0" )
		self.assertEqual(pHash,   27427800275512429 )
		self.assertEqual(imX,     493 )
		self.assertEqual(imY,     389)


	# check that phash is invariant across size changes
	def test_hashImage2_c(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		imPath = os.path.join(cwd, 'testimages', 'Lolcat_this_is_mah_job_small.jpg')

		with open(imPath, "rb") as fp:
			fCont = fp.read()

		basePath, intName = "LOL", "WAT.jpg"
		fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

		self.assertEqual(intName, fname)

		self.assertEqual(hexHash, "40d39c436e14282dcda06e8aff367307" )
		self.assertEqual(pHash,   27427800275512429 )
		self.assertEqual(imX,     300 )
		self.assertEqual(imY,     237)


	def test_hashImage3(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		imPath = os.path.join(cwd, 'testimages', 'lolcat-crocs.jpg')

		with open(imPath, "rb") as fp:
			fCont = fp.read()

		basePath, intName = "LOL", "WAT.jpg"
		fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

		self.assertEqual(intName, fname)

		self.assertEqual(hexHash, "6d0a977694630ac9d1d33a7f068e10f8" )
		self.assertEqual(pHash,   -5569898607211671279 )
		self.assertEqual(imX,     500 )
		self.assertEqual(imY,     363)


	def test_hashImage4(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		imPath = os.path.join(cwd, 'testimages', 'lolcat-oregon-trail.jpg')

		with open(imPath, "rb") as fp:
			fCont = fp.read()

		basePath, intName = "LOL", "WAT.jpg"
		fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

		self.assertEqual(intName, fname)

		self.assertEqual(hexHash, "7227289a017988b6bdcf61fd4761f6b9")
		self.assertEqual(pHash,   -4955310669995365332)
		self.assertEqual(imX,     501)
		self.assertEqual(imY,     356)


	def test_hashImage5(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		imPath = os.path.join(cwd, 'testimages', 'lolcat-oregon-trail.jpg')

		with open(imPath, "rb") as fp:
			fCont = fp.read()

		basePath, intName = "LOL", "WAT"
		fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

		self.assertEqual(intName, fname)

		self.assertEqual(hexHash, "7227289a017988b6bdcf61fd4761f6b9")
		self.assertEqual(pHash,   None)
		self.assertEqual(imX,     None)
		self.assertEqual(imY,     None)

	def test_hashImage6(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		imPath = os.path.join(cwd, 'testimages', 'lolcat-oregon-trail.jpg')

		with open(imPath, "rb") as fp:
			fCont = fp.read()

		basePath, intName = "LOL", "WAT.jpg"
		fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont, shouldPhash=False)

		self.assertEqual(intName, fname)

		self.assertEqual(hexHash, "7227289a017988b6bdcf61fd4761f6b9")
		self.assertEqual(pHash,   None)
		self.assertEqual(imX,     None)
		self.assertEqual(imY,     None)


	def test_hashFile(self):
		cwd = os.path.dirname(os.path.realpath(__file__))
		imPath = os.path.join(cwd, 'testimages', 'lolcat-oregon-trail.jpg')

		with open(imPath, "rb") as fp:
			fCont = fp.read()


		hexHash = phashlib.getMd5Hash(fCont)

		self.assertEqual(hexHash, "7227289a017988b6bdcf61fd4761f6b9")



	def test_hashImage6(self):
		cwd = os.path.dirname(os.path.realpath(__file__))

		images = [
				(
					'e61ec521-155d-4a3a-956d-2544d4367e02-ps.png',
					{
						'imY': 281,
						'hexHash': 'b4c3d02411a34e1222972cc262a40b89',
						'type': 'image/png',
						'imX': 375,
						# 'dHash': 5546533486212567551,
						'pHash': -4230769653536099758
					}
				),
			]

		for imgname, expect in images:
			imPath = os.path.join(cwd, 'testimages', imgname)

			with open(imPath, "rb") as fp:
				fCont = fp.read()

			basePath, intName = "LOL", imgname
			fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

			self.assertEqual(intName, fname)

			self.assertEqual(hexHash, expect['hexHash'])
			self.assertEqual(pHash,   expect['pHash'])
			self.assertEqual(imX,     expect['imX'])
			self.assertEqual(imY,     expect['imY'])

	def test_hashImage7(self):
		cwd = os.path.dirname(os.path.realpath(__file__))

		images = [
				(
					'funny-pictures-cat-looks-like-an-owl-ps.png',
					{
						'imY': 332,
						'hexHash': '740555f4e730ab2c6c261be7d53a3156',
						'type': 'image/png',
						'imX': 369,
						# 'dHash': -4629305759067799552,
						'pHash': -93277392328150
					}
				),
			]

		for imgname, expect in images:
			imPath = os.path.join(cwd, 'testimages', imgname)

			with open(imPath, "rb") as fp:
				fCont = fp.read()

			basePath, intName = "LOL", imgname
			fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

			self.assertEqual(intName, fname)

			self.assertEqual(hexHash, expect['hexHash'])
			self.assertEqual(pHash,   expect['pHash'])
			self.assertEqual(imX,     expect['imX'])
			self.assertEqual(imY,     expect['imY'])

	def test_hashImage8(self):
		cwd = os.path.dirname(os.path.realpath(__file__))

		images = [
				(
					'funny-pictures-cat-will-do-science-ps.png',
					{
						'imY': 506,
						'hexHash': 'c47ed1cd79c4e7925b8015cb51bbab10',
						'type': 'image/png',
						'imX': 375,
						# 'dHash': 1119025673978783491,
						'pHash': -6361731780925024615
					}
				)
			]

		for imgname, expect in images:
			imPath = os.path.join(cwd, 'testimages', imgname)

			with open(imPath, "rb") as fp:
				fCont = fp.read()

			basePath, intName = "LOL", imgname
			fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

			self.assertEqual(intName, fname)

			self.assertEqual(hexHash, expect['hexHash'])
			self.assertEqual(pHash,   expect['pHash'])
			self.assertEqual(imX,     expect['imX'])
			self.assertEqual(imY,     expect['imY'])

	def test_hashImage9(self):
		cwd = os.path.dirname(os.path.realpath(__file__))

		images = [
				(
					'funny-pictures-kitten-rules-a-tower-ps.png',
					{
						'imY': 281,
						'hexHash': 'fb64248009dde8605a95b041b772544a',
						'type': 'image/png',
						'imX': 375,
						# 'dHash': 9187567978625498130,
						'pHash': -5860684349360469885
					}
				)
			]

		for imgname, expect in images:
			imPath = os.path.join(cwd, 'testimages', imgname)

			with open(imPath, "rb") as fp:
				fCont = fp.read()

			basePath, intName = "LOL", imgname
			fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

			self.assertEqual(intName, fname)

			self.assertEqual(hexHash, expect['hexHash'])
			self.assertEqual(pHash,   expect['pHash'])
			self.assertEqual(imX,     expect['imX'])
			self.assertEqual(imY,     expect['imY'])

	def test_hashImage10(self):
		cwd = os.path.dirname(os.path.realpath(__file__))

		images = [
				('superheroes-batman-superman-i-would-watch-the-hell-out-of-this.jpg',
					{
						'hexHash': '083e179ff11ccf90a0d514651c69c2ca',
						'imX': 200,
						'imY': 297,
						'pHash': -8034280126218048380,
						'type': 'image/jpeg'
					}
				)
			]

		for imgname, expect in images:
			imPath = os.path.join(cwd, 'testimages', imgname)

			with open(imPath, "rb") as fp:
				fCont = fp.read()

			basePath, intName = "LOL", imgname
			fname, hexHash, pHash, imX, imY = phashlib.hashFile(basePath, intName, fCont)

			self.assertEqual(intName, fname)

			self.assertEqual(hexHash, expect['hexHash'])
			self.assertEqual(pHash,   expect['pHash'])
			self.assertEqual(imX,     expect['imX'])
			self.assertEqual(imY,     expect['imY'])
