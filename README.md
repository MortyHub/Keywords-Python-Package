# Keyword Package
**This is a tool that will make keyword managing so much easier, this can be used in things for online marketing for ads and much more!**
## Use
**To import simply use `from Keyword import *`. To create a keyword use:**
```py
# Example will become the keyword object
Example = Keywords("Name", "Key")
```
**We can set a an already existing key using:**
```py
# Example object self changing
Example.setKey("Key")
```
**We can also grab the key using:**
```py
# Example object getting self key
Example.getKey()
```
**We can get the name of a key**:
```py
# Example object getting self name
Example.getName()
```
**We can detect a key's use with:**
```py
# Will return True
Example.testKey("Key")
```
**We can test for the name of a key with:**
```py
# will return True
Example.testName("Name")
```
**We can delete a tag using:**
```py
Example.remove()
```
**We can set the name of an item using:**
```py
Example.setName("New-Name")
```