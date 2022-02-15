# protobuf-custom-build

This is a small package that allows a repository containing only protobuf
definitions to be used in a Python project via `pip install`. Please see
[python-protobuf-repo-examle](https://github.com/sbrother/python-protobuf-repo-example)
for a full example of a protobuf repo using this package; it boils down to
including the line

```
distutils.command.build.build.sub_commands.insert(0, ('protobuf-custom-build', None))
```

in your `setup.py`.
