# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_Aono')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_Aono')
    _Aono = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Aono', [dirname(__file__)])
        except ImportError:
            import _Aono
            return _Aono
        try:
            _mod = imp.load_module('_Aono', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _Aono = swig_import_helper()
    del swig_import_helper
else:
    import _Aono
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def pari_init(parisize, maxprime):
    return _Aono.pari_init(parisize, maxprime)
pari_init = _Aono.pari_init

def pari_close():
    return _Aono.pari_close()
pari_close = _Aono.pari_close
class ciphertext(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ciphertext, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ciphertext, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _Aono.ciphertext_value_set
    __swig_getmethods__["value"] = _Aono.ciphertext_value_get
    if _newclass:
        value = _swig_property(_Aono.ciphertext_value_get, _Aono.ciphertext_value_set)
    __swig_setmethods__["degree"] = _Aono.ciphertext_degree_set
    __swig_getmethods__["degree"] = _Aono.ciphertext_degree_get
    if _newclass:
        degree = _swig_property(_Aono.ciphertext_degree_get, _Aono.ciphertext_degree_set)
    __swig_setmethods__["pk"] = _Aono.ciphertext_pk_set
    __swig_getmethods__["pk"] = _Aono.ciphertext_pk_get
    if _newclass:
        pk = _swig_property(_Aono.ciphertext_pk_get, _Aono.ciphertext_pk_set)
    __swig_setmethods__["params"] = _Aono.ciphertext_params_set
    __swig_getmethods__["params"] = _Aono.ciphertext_params_get
    if _newclass:
        params = _swig_property(_Aono.ciphertext_params_get, _Aono.ciphertext_params_set)
    __swig_destroy__ = _Aono.delete_ciphertext
    __del__ = lambda self: None

    def packing_method(self, m, pk):
        return _Aono.ciphertext_packing_method(self, m, pk)

    def initialize(self, *args):
        return _Aono.ciphertext_initialize(self, *args)

    def __add__(self, ct):
        return _Aono.ciphertext___add__(self, ct)

    def __sub__(self, ct):
        return _Aono.ciphertext___sub__(self, ct)

    def decrypt(self, sk):
        return _Aono.ciphertext_decrypt(self, sk)

    def __init__(self, *args):
        this = _Aono.new_ciphertext(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __mul__(self, *args):
        return _Aono.ciphertext___mul__(self, *args)

    def __rmul__(self, pt):
        return _Aono.ciphertext___rmul__(self, pt)
ciphertext_swigregister = _Aono.ciphertext_swigregister
ciphertext_swigregister(ciphertext)

class updation_key(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, updation_key, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, updation_key, name)
    __repr__ = _swig_repr
    __swig_setmethods__["params"] = _Aono.updation_key_params_set
    __swig_getmethods__["params"] = _Aono.updation_key_params_get
    if _newclass:
        params = _swig_property(_Aono.updation_key_params_get, _Aono.updation_key_params_set)
    __swig_setmethods__["params_old"] = _Aono.updation_key_params_old_set
    __swig_getmethods__["params_old"] = _Aono.updation_key_params_old_get
    if _newclass:
        params_old = _swig_property(_Aono.updation_key_params_old_get, _Aono.updation_key_params_old_set)
    __swig_setmethods__["g"] = _Aono.updation_key_g_set
    __swig_getmethods__["g"] = _Aono.updation_key_g_get
    if _newclass:
        g = _swig_property(_Aono.updation_key_g_get, _Aono.updation_key_g_set)

    def __init__(self, *args):
        this = _Aono.new_updation_key(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def initialize(self, X, Y, params, params_old, g, pk):
        return _Aono.updation_key_initialize(self, X, Y, params, params_old, g, pk)

    def cipher_switch(self, ct):
        return _Aono.updation_key_cipher_switch(self, ct)

    def serialize(self):
        return _Aono.updation_key_serialize(self)
    __swig_destroy__ = _Aono.delete_updation_key
    __del__ = lambda self: None
updation_key_swigregister = _Aono.updation_key_swigregister
updation_key_swigregister(updation_key)

class updation_key_gen(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, updation_key_gen, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, updation_key_gen, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _Aono.new_updation_key_gen()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def generate_key(self, key1, key2):
        return _Aono.updation_key_gen_generate_key(self, key1, key2)
    __swig_destroy__ = _Aono.delete_updation_key_gen
    __del__ = lambda self: None
updation_key_gen_swigregister = _Aono.updation_key_gen_swigregister
updation_key_gen_swigregister(updation_key_gen)

class secret_key(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, secret_key, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, secret_key, name)
    __repr__ = _swig_repr
    __swig_setmethods__["params"] = _Aono.secret_key_params_set
    __swig_getmethods__["params"] = _Aono.secret_key_params_get
    if _newclass:
        params = _swig_property(_Aono.secret_key_params_get, _Aono.secret_key_params_set)

    def __init__(self, *args):
        this = _Aono.new_secret_key(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def initialize(self, sk, params):
        return _Aono.secret_key_initialize(self, sk, params)

    def decrypt(self, ct):
        return _Aono.secret_key_decrypt(self, ct)

    def serialize(self):
        return _Aono.secret_key_serialize(self)
    __swig_destroy__ = _Aono.delete_secret_key
    __del__ = lambda self: None
secret_key_swigregister = _Aono.secret_key_swigregister
secret_key_swigregister(secret_key)

class public_key(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, public_key, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, public_key, name)
    __repr__ = _swig_repr
    __swig_setmethods__["params"] = _Aono.public_key_params_set
    __swig_getmethods__["params"] = _Aono.public_key_params_get
    if _newclass:
        params = _swig_property(_Aono.public_key_params_get, _Aono.public_key_params_set)
    __swig_setmethods__["g"] = _Aono.public_key_g_set
    __swig_getmethods__["g"] = _Aono.public_key_g_get
    if _newclass:
        g = _swig_property(_Aono.public_key_g_get, _Aono.public_key_g_set)

    def __init__(self, *args):
        this = _Aono.new_public_key(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def initialize(self, pk, params, g):
        return _Aono.public_key_initialize(self, pk, params, g)

    def encrypt(self, m):
        return _Aono.public_key_encrypt(self, m)

    def serialize(self):
        return _Aono.public_key_serialize(self)
    __swig_destroy__ = _Aono.delete_public_key
    __del__ = lambda self: None
public_key_swigregister = _Aono.public_key_swigregister
public_key_swigregister(public_key)

class key_pair(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, key_pair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, key_pair, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sk"] = _Aono.key_pair_sk_set
    __swig_getmethods__["sk"] = _Aono.key_pair_sk_get
    if _newclass:
        sk = _swig_property(_Aono.key_pair_sk_get, _Aono.key_pair_sk_set)
    __swig_setmethods__["pk"] = _Aono.key_pair_pk_set
    __swig_getmethods__["pk"] = _Aono.key_pair_pk_get
    if _newclass:
        pk = _swig_property(_Aono.key_pair_pk_get, _Aono.key_pair_pk_set)

    def __init__(self):
        this = _Aono.new_key_pair()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Aono.delete_key_pair
    __del__ = lambda self: None
key_pair_swigregister = _Aono.key_pair_swigregister
key_pair_swigregister(key_pair)

class key_gen(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, key_gen, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, key_gen, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _Aono.new_key_gen()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def generate_key(self, arg2, l, n, s, sigma, degree_p):
        return _Aono.key_gen_generate_key(self, arg2, l, n, s, sigma, degree_p)
    __swig_destroy__ = _Aono.delete_key_gen
    __del__ = lambda self: None
key_gen_swigregister = _Aono.key_gen_swigregister
key_gen_swigregister(key_gen)

M_PI = _Aono.M_PI
precision = _Aono.precision
class pari_GEN(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pari_GEN, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pari_GEN, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _Aono.pari_GEN_value_set
    __swig_getmethods__["value"] = _Aono.pari_GEN_value_get
    if _newclass:
        value = _swig_property(_Aono.pari_GEN_value_get, _Aono.pari_GEN_value_set)

    def initialize(self, x):
        return _Aono.pari_GEN_initialize(self, x)

    def __add__(self, GEN_2):
        return _Aono.pari_GEN___add__(self, GEN_2)

    def __mul__(self, GEN_2):
        return _Aono.pari_GEN___mul__(self, GEN_2)

    def __truediv__(self, *args):
        return _Aono.pari_GEN___truediv__(self, *args)
    __div__ = __truediv__



    def __sub__(self, GEN_2):
        return _Aono.pari_GEN___sub__(self, GEN_2)

    def __mod__(self, GEN_2):
        return _Aono.pari_GEN___mod__(self, GEN_2)

    def __eq__(self, GEN_2):
        return _Aono.pari_GEN___eq__(self, GEN_2)

    def __init__(self, *args):
        this = _Aono.new_pari_GEN(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __str__(self):
        return _Aono.pari_GEN___str__(self)

    def __getitem__(self, key):
        return _Aono.pari_GEN___getitem__(self, key)

    def sub_mat_array(self, *args):
        return _Aono.pari_GEN_sub_mat_array(self, *args)

    def sub_array(self, key_1, key_2):
        return _Aono.pari_GEN_sub_array(self, key_1, key_2)
    __swig_destroy__ = _Aono.delete_pari_GEN
    __del__ = lambda self: None
pari_GEN_swigregister = _Aono.pari_GEN_swigregister
pari_GEN_swigregister(pari_GEN)
cvar = _Aono.cvar

class parameters(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, parameters, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, parameters, name)
    __repr__ = _swig_repr
    __swig_setmethods__["q"] = _Aono.parameters_q_set
    __swig_getmethods__["q"] = _Aono.parameters_q_get
    if _newclass:
        q = _swig_property(_Aono.parameters_q_get, _Aono.parameters_q_set)
    __swig_setmethods__["p"] = _Aono.parameters_p_set
    __swig_getmethods__["p"] = _Aono.parameters_p_get
    if _newclass:
        p = _swig_property(_Aono.parameters_p_get, _Aono.parameters_p_set)
    __swig_setmethods__["_lambda"] = _Aono.parameters__lambda_set
    __swig_getmethods__["_lambda"] = _Aono.parameters__lambda_get
    if _newclass:
        _lambda = _swig_property(_Aono.parameters__lambda_get, _Aono.parameters__lambda_set)
    __swig_setmethods__["l"] = _Aono.parameters_l_set
    __swig_getmethods__["l"] = _Aono.parameters_l_get
    if _newclass:
        l = _swig_property(_Aono.parameters_l_get, _Aono.parameters_l_set)
    __swig_setmethods__["s"] = _Aono.parameters_s_set
    __swig_getmethods__["s"] = _Aono.parameters_s_get
    if _newclass:
        s = _swig_property(_Aono.parameters_s_get, _Aono.parameters_s_set)
    __swig_setmethods__["n"] = _Aono.parameters_n_set
    __swig_getmethods__["n"] = _Aono.parameters_n_get
    if _newclass:
        n = _swig_property(_Aono.parameters_n_get, _Aono.parameters_n_set)
    __swig_setmethods__["sigma"] = _Aono.parameters_sigma_set
    __swig_getmethods__["sigma"] = _Aono.parameters_sigma_get
    if _newclass:
        sigma = _swig_property(_Aono.parameters_sigma_get, _Aono.parameters_sigma_set)

    def __init__(self):
        this = _Aono.new_parameters()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Aono.delete_parameters
    __del__ = lambda self: None
parameters_swigregister = _Aono.parameters_swigregister
parameters_swigregister(parameters)

class ProbMatrixPack(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ProbMatrixPack, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ProbMatrixPack, name)
    __repr__ = _swig_repr
    __swig_setmethods__["P"] = _Aono.ProbMatrixPack_P_set
    __swig_getmethods__["P"] = _Aono.ProbMatrixPack_P_get
    if _newclass:
        P = _swig_property(_Aono.ProbMatrixPack_P_get, _Aono.ProbMatrixPack_P_set)
    __swig_setmethods__["startPos"] = _Aono.ProbMatrixPack_startPos_set
    __swig_getmethods__["startPos"] = _Aono.ProbMatrixPack_startPos_get
    if _newclass:
        startPos = _swig_property(_Aono.ProbMatrixPack_startPos_get, _Aono.ProbMatrixPack_startPos_set)
    __swig_setmethods__["isInitialized"] = _Aono.ProbMatrixPack_isInitialized_set
    __swig_getmethods__["isInitialized"] = _Aono.ProbMatrixPack_isInitialized_get
    if _newclass:
        isInitialized = _swig_property(_Aono.ProbMatrixPack_isInitialized_get, _Aono.ProbMatrixPack_isInitialized_set)

    def __init__(self):
        this = _Aono.new_ProbMatrixPack()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Aono.delete_ProbMatrixPack
    __del__ = lambda self: None
ProbMatrixPack_swigregister = _Aono.ProbMatrixPack_swigregister
ProbMatrixPack_swigregister(ProbMatrixPack)

class public_key_pack(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, public_key_pack, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, public_key_pack, name)
    __repr__ = _swig_repr
    __swig_setmethods__["A"] = _Aono.public_key_pack_A_set
    __swig_getmethods__["A"] = _Aono.public_key_pack_A_get
    if _newclass:
        A = _swig_property(_Aono.public_key_pack_A_get, _Aono.public_key_pack_A_set)
    __swig_setmethods__["P"] = _Aono.public_key_pack_P_set
    __swig_getmethods__["P"] = _Aono.public_key_pack_P_get
    if _newclass:
        P = _swig_property(_Aono.public_key_pack_P_get, _Aono.public_key_pack_P_set)
    __swig_setmethods__["n"] = _Aono.public_key_pack_n_set
    __swig_getmethods__["n"] = _Aono.public_key_pack_n_get
    if _newclass:
        n = _swig_property(_Aono.public_key_pack_n_get, _Aono.public_key_pack_n_set)
    __swig_setmethods__["s"] = _Aono.public_key_pack_s_set
    __swig_getmethods__["s"] = _Aono.public_key_pack_s_get
    if _newclass:
        s = _swig_property(_Aono.public_key_pack_s_get, _Aono.public_key_pack_s_set)

    def __init__(self):
        this = _Aono.new_public_key_pack()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Aono.delete_public_key_pack
    __del__ = lambda self: None
public_key_pack_swigregister = _Aono.public_key_pack_swigregister
public_key_pack_swigregister(public_key_pack)

class globalvars(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, globalvars, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, globalvars, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pPack"] = _Aono.globalvars_pPack_set
    __swig_getmethods__["pPack"] = _Aono.globalvars_pPack_get
    if _newclass:
        pPack = _swig_property(_Aono.globalvars_pPack_get, _Aono.globalvars_pPack_set)
    __swig_setmethods__["errorsModulo"] = _Aono.globalvars_errorsModulo_set
    __swig_getmethods__["errorsModulo"] = _Aono.globalvars_errorsModulo_get
    if _newclass:
        errorsModulo = _swig_property(_Aono.globalvars_errorsModulo_get, _Aono.globalvars_errorsModulo_set)

    def __init__(self):
        this = _Aono.new_globalvars()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Aono.delete_globalvars
    __del__ = lambda self: None
globalvars_swigregister = _Aono.globalvars_swigregister
globalvars_swigregister(globalvars)

class cipher_text(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cipher_text, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cipher_text, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flag"] = _Aono.cipher_text_flag_set
    __swig_getmethods__["flag"] = _Aono.cipher_text_flag_get
    if _newclass:
        flag = _swig_property(_Aono.cipher_text_flag_get, _Aono.cipher_text_flag_set)
    __swig_setmethods__["comp1"] = _Aono.cipher_text_comp1_set
    __swig_getmethods__["comp1"] = _Aono.cipher_text_comp1_get
    if _newclass:
        comp1 = _swig_property(_Aono.cipher_text_comp1_get, _Aono.cipher_text_comp1_set)
    __swig_setmethods__["comp2"] = _Aono.cipher_text_comp2_set
    __swig_getmethods__["comp2"] = _Aono.cipher_text_comp2_get
    if _newclass:
        comp2 = _swig_property(_Aono.cipher_text_comp2_get, _Aono.cipher_text_comp2_set)

    def __init__(self):
        this = _Aono.new_cipher_text()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Aono.delete_cipher_text
    __del__ = lambda self: None
cipher_text_swigregister = _Aono.cipher_text_swigregister
cipher_text_swigregister(cipher_text)

class cipher_text_mult(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cipher_text_mult, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cipher_text_mult, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flag"] = _Aono.cipher_text_mult_flag_set
    __swig_getmethods__["flag"] = _Aono.cipher_text_mult_flag_get
    if _newclass:
        flag = _swig_property(_Aono.cipher_text_mult_flag_get, _Aono.cipher_text_mult_flag_set)
    __swig_setmethods__["c"] = _Aono.cipher_text_mult_c_set
    __swig_getmethods__["c"] = _Aono.cipher_text_mult_c_get
    if _newclass:
        c = _swig_property(_Aono.cipher_text_mult_c_get, _Aono.cipher_text_mult_c_set)

    def __init__(self):
        this = _Aono.new_cipher_text_mult()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Aono.delete_cipher_text_mult
    __del__ = lambda self: None
cipher_text_mult_swigregister = _Aono.cipher_text_mult_swigregister
cipher_text_mult_swigregister(cipher_text_mult)


def get_element(*args):
    return _Aono.get_element(*args)
get_element = _Aono.get_element

def print_GEN(*args):
    return _Aono.print_GEN(*args)
print_GEN = _Aono.print_GEN

def create_GEN(*args):
    return _Aono.create_GEN(*args)
create_GEN = _Aono.create_GEN

def Uniform():
    return _Aono.Uniform()
Uniform = _Aono.Uniform

def Normal():
    return _Aono.Normal()
Normal = _Aono.Normal

def Gauss(mu, sigma):
    return _Aono.Gauss(mu, sigma)
Gauss = _Aono.Gauss

def Sample(n, sigma):
    return _Aono.Sample(n, sigma)
Sample = _Aono.Sample

def generate_random(bit_length):
    return _Aono.generate_random(bit_length)
generate_random = _Aono.generate_random

def getGuassProbability(point, center, params):
    return _Aono.getGuassProbability(point, center, params)
getGuassProbability = _Aono.getGuassProbability

def genProbabilityMatrix(*args):
    return _Aono.genProbabilityMatrix(*args)
genProbabilityMatrix = _Aono.genProbabilityMatrix

def SampleKnuthYao(c, params, g):
    return _Aono.SampleKnuthYao(c, params, g)
SampleKnuthYao = _Aono.SampleKnuthYao

def initialize_sampler(*args):
    return _Aono.initialize_sampler(*args)
initialize_sampler = _Aono.initialize_sampler

def getGENsize(x):
    return _Aono.getGENsize(x)
getGENsize = _Aono.getGENsize

def getGEN_MATRIXsize(x):
    return _Aono.getGEN_MATRIXsize(x)
getGEN_MATRIXsize = _Aono.getGEN_MATRIXsize

def generate_secret_key(*args):
    return _Aono.generate_secret_key(*args)
generate_secret_key = _Aono.generate_secret_key

def generate_public_key(*args):
    return _Aono.generate_public_key(*args)
generate_public_key = _Aono.generate_public_key

def set_error_modulo(g, modulo):
    return _Aono.set_error_modulo(g, modulo)
set_error_modulo = _Aono.set_error_modulo

def access_value_pk(pk, flag):
    return _Aono.access_value_pk(pk, flag)
access_value_pk = _Aono.access_value_pk

def gen_params(arg1, l, n, s, sigma, degree_p):
    return _Aono.gen_params(arg1, l, n, s, sigma, degree_p)
gen_params = _Aono.gen_params

def create_message_matrix_repeated_input(arg1, arg2):
    return _Aono.create_message_matrix_repeated_input(arg1, arg2)
create_message_matrix_repeated_input = _Aono.create_message_matrix_repeated_input

def multiplication(arg1, arg2, arg3):
    return _Aono.multiplication(arg1, arg2, arg3)
multiplication = _Aono.multiplication

def encrypt_outside_class(m, pk, params, g):
    return _Aono.encrypt_outside_class(m, pk, params, g)
encrypt_outside_class = _Aono.encrypt_outside_class

def addition(ct_1, ct_2, params, pk, g):
    return _Aono.addition(ct_1, ct_2, params, pk, g)
addition = _Aono.addition

def subtraction(ct_1, ct_2, params, pk, g):
    return _Aono.subtraction(ct_1, ct_2, params, pk, g)
subtraction = _Aono.subtraction

def create_message_matrix(*args):
    return _Aono.create_message_matrix(*args)
create_message_matrix = _Aono.create_message_matrix

def see_ciphertext(c, index):
    return _Aono.see_ciphertext(c, index)
see_ciphertext = _Aono.see_ciphertext

def power2(x, n, kappa, l, q):
    return _Aono.power2(x, n, kappa, l, q)
power2 = _Aono.power2

def appendmat(m1, m2, col1, col2, row):
    return _Aono.appendmat(m1, m2, col1, col2, row)
appendmat = _Aono.appendmat

def bits(m, kappa, n):
    return _Aono.bits(m, kappa, n)
bits = _Aono.bits

def get_updation_parameters(params_old, n, s):
    return _Aono.get_updation_parameters(params_old, n, s)
get_updation_parameters = _Aono.get_updation_parameters

def plaintext_multiplication(ct, input):
    return _Aono.plaintext_multiplication(ct, input)
plaintext_multiplication = _Aono.plaintext_multiplication

import atexit
pari_init(2000000000, 2)
atexit.register(pari_close)

class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _Aono.new_intArray(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Aono.delete_intArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _Aono.intArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _Aono.intArray___setitem__(self, index, value)

    def cast(self):
        return _Aono.intArray_cast(self)
    if _newclass:
        frompointer = staticmethod(_Aono.intArray_frompointer)
    else:
        frompointer = _Aono.intArray_frompointer
intArray_swigregister = _Aono.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(t):
    return _Aono.intArray_frompointer(t)
intArray_frompointer = _Aono.intArray_frompointer

# This file is compatible with both classic and new-style classes.


