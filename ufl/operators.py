"""This module extends the form language with free function operators,
which are either already available as member functions on UFL objects
or defined as compound operators involving basic operations on the UFL
objects."""

__authors__ = "Martin Sandve Alnes and Anders Logg"
__date__ = "2008-04-09 -- 2008-04-09"

from base import Transpose
from differentiation import Grad, Div, Curl, Rot
from tensoralgebra import Inner, Outer, Dot, Cross, Determinant, Trace, Deviatoric, Cofactor

#--- Algebraic operators ---

# FIXME: This is a tensor operator?
def transp(o):
    "Return transpose of expression"
    return Transpose(o)

def abs(o):
    return Abs(o)

#--- Tensor operators ---

def outer(a, b):
    return Outer(a, b)

def inner(a, b):
    return Inner(a, b)

def dot(a, b):
    return Dot(a, b)

def cross(a, b):
    return Cross(a, b)

def det(f):
    return Determinant(f)

def inv(f):
    return Inverse(f)

def tr(f):
    return Trace(f)

def dev(A):
    return Deviatoric(A)

def cofac(A):
    return Cofactor(A)

#--- Differential operators

def Dx(o, i):
    """Return the partial derivative with respect to spatial variable number i"""
    # FIXME: Should be class as for other operators
    #return SpatialDerivative(o, i)
    return f.dx(i)

def Dt(o):
    # FIXME: Add class
    #return TimeDerivative(o)
    return 0

def grad(f):
    return Grad(f)

def div(f):
    return Div(f)

def curl(f):
    return Curl(f)

def rot(f):
    return Rot(f)

#--- DG operators ---

def jump(o):
    raise NotImplementedError

def avg(o):
    raise NotImplementedError

#--- Suggestions ---

def sqrt(o):
    raise NotImplementedError
