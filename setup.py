from distutils.core import setup

setup(
    name="s3lowbe",
    py_modules=["s3lowbe"],
    entry_points={"console_scripts": ["s3lowbe=s3lowbe:main"]},
    version="0.2.0",
    description="Low bandwidth DoS tool. s3lowbe rewrite in Python.",
    author="Rex4",
    author_email="cantixcr3w@yahoo.com",
    url="https://github.com/cantix/s3lowbe",
    keywords=["dos", "http", "s3lowbe"],
)
