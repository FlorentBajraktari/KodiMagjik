from setuptools import setup, find_packages

setup(
    name='KodiMagjik',
    version='1.0',
    packages=find_packages(),  # Automatizon gjetjen e dosjes së paketës
    install_requires=[
        'kivy',
        'kivymd',
        # Shto varësi të tjera këtu nëse ka
    ],
    entry_points={
        'console_scripts': [
            # Referohet te klasa kryesore e aplikacionit
            'kodimagjik=kodimagjik.main:KodiMagjikApp',
        ],
    },
)
