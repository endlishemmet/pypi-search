# pypi-search
The pypi search engine based on requests and BeautifulSoup.

## Usage:
```py
from src.search import Package

pkg = Package()
toml = pkg.search("toml")["Project.Description"]
print(toml)
```

1. Create a variable with type Package
```py
pkg = Package()
```
2. Search
`search` method searches a package that specified and it's returns dictionary with keys:
+ `name` &mdash; a name of package
+ `Project.Description` &mdash; a description of package
+ `Release.TimeLine` &mdash; a release timeline
+ `Release.TimeLine.Current.Version` &mdash; a current version of package
+ `Release.TimeLine.Current.Date` &mdash; a date of current version of package

```py
pkg.search("flask")
```
3. Install
`install` method installs a package.

```py
pkg.install("flask")
```
4. Include
`include` method import a package

```py
pkg.include("flask")
```