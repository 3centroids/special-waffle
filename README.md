> **NOTE**
> Due to portability issues, the repository is going to be archived. A simpler version written in `bash` is [here](https://github.com/3centroids/glowing-carnival)!

# local-test

Portable local testing software (and test case generator TODO: implement this) written in Python for competitive programming in C++.

## Platform support

Unix-like (e.g. macOS, Linux) uses bash and Windows uses Command Prompt.

| platform | Unix-like | Windows | WSL2 |
|:---:|:---:|:---:|:---:|
| support | :heavy_check_mark: | :heavy_check_mark: | :x: |
| shell | bash | cmd | bash |

## Usage

example folder structure
```
.
└── foo/
    ├── bar-tests/
    │   ├── 0.in
    │   └── 0.out
    └── bar.cpp
```

output generated with ```-h```
```
usage: lt.py [-h] -p PROGRAM [-c]

optional arguments:
  -h, --help            show this help message and exit
  -p PROGRAM, --program PROGRAM
                        program pathname
  -c, --compile         compile program (default=False)
```

### Unix-like
```python3 $lt/lt.py -p bar.cpp -c```\
For simplicity, setup an environment variable for your local-test directory.

```bash
echo "export VARIABLE_NAME=value" >> ~/.bash_profile
```

### Windows
```python %lt%\lt.py -p bar.cpp -c```\
Unless local-test directory is an environment variable ("lt"), replace "%lt%\lt.py" with its pathname.

Environment Variables > System variables > New

### Writing test cases

> **IMPORTANT**
> Make sure to have matching newlines, otherwise correct output might flag your program as defective. Example below.

```bar.cpp```
```cpp
#include <cstdio>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", n);
}
```

^ Newline character present

```0.in```
```
66

```

^ Would work without newline

```0.out```
```
66

```

^ Newline present

<strike>
## Why Python?

[SIO2](https://github.com/sio2project) (used by [POI](https://oi.edu.pl) ([POI's SIO2 link](https://sio2.mimuw.edu.pl/))) itself is partially written in Python. Honestly, I found joy writing Python for a change.
BTW check out similar testing program written in bash shell ([link](https://example.com)).
</strike>

## Configuration - ```config.json```

> **WARNING**
> Specified compiler will be run in shell.

### Valid key options

(not actual JSON below)

```json
"platform": ["Unix", "Windows"]
"compiler": ["clang++", "clang", "g++", "gcc", "etc."]
"generator-prefix": ["gen", "g", "etc."]
```

## TODO

[Known issues and future improvements](docs/TODO.md)

## Contributing

[Contribution guidelines for this project](docs/CONTRIBUTING.md)
