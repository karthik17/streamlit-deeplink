from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='streamlit-deeplink',
    version='1.0.1',
    license='MIT',
    description="Streamlit add on to deep link widget selections into url query parameters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Karthik Nichenametla",
    author_email='etherxplorer21@example.com',
    packages=find_packages(),
    url='https://github.com/karthik17/streamlit-deeplink',
    python_requires='>=3.6',
    install_requires=[
          'streamlit >= 1.0.0',
      ],

)

