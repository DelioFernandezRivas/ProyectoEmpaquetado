from distutils.core import setup

#from setuptools import setup.find.packages
ficheiros = ["cousas/*"]

setup (name = "proba",
       version = "0.01",
       description = "Aplicación de exemplo de distribución",
       long_description = """ descripcion 
    en mais de una linea onde pordemos por todo o que queramos""",
       author = "Diego",
       author_email = "dalonsoperez@danielcastelao.org",
       url = "www.patatitabailonga.wordpress.com",
       keywords = "proba, distribución, exemplo",
       platforms = "linux, mac",
       #packages = ['paquetes'],
       #packages= find.packates(),
       package_data = {'paquete': ficheiros},
       scripts = ["lanzador"],
       py_modules = ["moduloForaDePaquete"])