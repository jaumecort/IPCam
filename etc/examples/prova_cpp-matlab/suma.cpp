/*
* arrayProduct.cpp - example in MATLAB External Interfaces
*
* Multiplies an input scalar (multiplier)
* times a MxN matrix (inMatrix)
* and outputs a MxN matrix (outMatrix)
*
* Usage : from MATLAB
*         >> outMatrix = arrayProduct(multiplier, inMatrix)
*
* This is a C++ MEX-file for MATLAB.
* Copyright 2017 The MathWorks, Inc.
*
*/

#include "mex.hpp"
#include "mexAdapter.hpp"

class MexFunction : public matlab::mex::Function {
public:
    void operator()(matlab::mex::ArgumentList outputs, matlab::mex::ArgumentList inputs) {
        mexPrintf("he");
    }
};