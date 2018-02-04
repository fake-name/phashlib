
## PHashLib


Basically [ImageHash](https://github.com/JohannesBuchner/imagehash), but with 
some additional utility functions, and more testing.

The motivation behind this package is that there are a lot of variables that affect
the behaviour of the p-hashing, and I have had upstream packages break things. 

There have been several instances where changes in PIL/pillow have caused the 
unit-tests in my [deduplicator prject](https://github.com/fake-name/IntraArchiveDeduplicator)
to fail, and now that I want to do phash-checking in multiple projects, I figure 
it's an appropriate time to split it out into an actual package.

All the actual hard-work was done by the package this is derived from, principally
by [@JohannesBuchner](https://github.com/JohannesBuchner).