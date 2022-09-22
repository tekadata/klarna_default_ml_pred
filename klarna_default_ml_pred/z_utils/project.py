from  os.path import abspath, normpath, join, dirname
# you can check your pythonpath specifically
import os;
## To use this library inside the project klarna_default_ml_pred uncomment:
# import klarna_default_ml_pred.z_utils.project as uz
## Then call insight function with uz.get_<my_function>("dir1", "dir2")
## With optional parameter list of chained directories (use ".." to go to parent)

def get_py_path(*args) -> str:
    return get_abs_path(join(os.environ['PYTHONPATH'], *args))


def get_abs_path(*args) -> str:
    return abspath(join(dirname(__file__), *args))


def get_normpath(*args) -> str:
    return normpath(join(dirname(__file__), *args))


def get_csv_out_path() -> str:
    return get_abs_path(join(get_py_path(), "klarna_default_ml_pred", "a_data", "aa_out_csv"))


def get_raw_data_path(*args) -> str:
    return normpath(join(get_py_path(), "raw_data", *args))
