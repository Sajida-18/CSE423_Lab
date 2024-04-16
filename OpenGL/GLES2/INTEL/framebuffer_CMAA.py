'''OpenGL extension INTEL.framebuffer_CMAA

This module customises the behaviour of the 
OpenGL.raw.GLES2.INTEL.framebuffer_CMAA to provide a more 
Python-friendly API

Overview (from the spec)
	
	Multisampling is a mechanism to antialias all GL primitives and is part of
	the GL specification.
	
	Better visual quality can be achieved by applying multisampling. However,
	on certain platforms it comes at a high performance cost. In general, the
	greater number of samples per pixel, the bigger the cost.
	
	Conservative Morphological Anti-Aliasing (CMAA) is an alternative approach
	to antialiasing, which operates on the final image. This post processing
	technique results in image quality comparable to multisampling at much
	lower cost and better performance.
	
	This extension incorporates an optimized CMAA algorithm implementation into
	the GL implementation.
	
	For more information on CMAA refer to http://software.intel.com.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/INTEL/framebuffer_CMAA.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.INTEL.framebuffer_CMAA import *
from OpenGL.raw.GLES2.INTEL.framebuffer_CMAA import _EXTENSION_NAME

def glInitFramebufferCmaaINTEL():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION