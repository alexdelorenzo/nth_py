from setuptools import setup
from pathlib import Path

requirements = Path('requirements.txt').read_text().split('\n')
readme = Path('README.md').read_text()


setup(name="nth_py",
      version="0.0.2",
      description="Return or exclude the nth item via stdin",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://alexdelorenzo.dev",
      author="Alex DeLorenzo",
      license="AGPL-3.0",
      packages=['nth_py'],
      zip_safe=True,
      install_requires=requirements,
      python_requires='>=3.6',
      entry_points={"console_scripts":
                        ["nth = nth_py.nth:cmd"]},
)
