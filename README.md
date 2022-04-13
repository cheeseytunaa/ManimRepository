# DeepFriedTunaa's Manim Repository
##### A repository in which I store and develop mathematics videos using the Manim-ation library!

## What da hell is this :)?
- This is the place where I put all of my codes using Manim to render Math-videos.
- Due to the conveniences, I will not have to worry about my codes will be deleted, also it's so easy to manage, edit, maintain them. Yet one more reason is for everyone to use my code freely.

## Features

- I use the Manim library (*Community Edition*), a community-maintained version of the original Manim by 3b1b.
- You can just use my code, download and render them, it's that simple. Or edit them for your own purposes.
- Always be updated (at least weekly or monthly), a rich repository which contains a great number of Mathematics videos.
- Each folder consists of one main code file (or more, depending on the main one), one .mp4 result file.


## What is Viettex?
- `VietTex` (or `Viettex`, `viettex`, ...) is an additional python library file which is used to support `Vietnamese-UTF8-characters` in `LaTeX`, moreover even `TeX`.
- How to use it? : Really easy, put the viettex.py file in the namespace folder, use this command to import the file:
```
from viettex import *
```
and to use, simply use the `VietTex()` class:
```
test_viet_tex = VietTex(r"$\LaTeX$")
test_viet_tex_2 = VietTex(r"ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ")
```

## How to render?
- Very good question! As normal, we can use the terminal command:
```
manim <filename>.py (OPTIONAL_SCENE_INDEX_NUMBER/NAME) (OPTIONAL_ARGUMENTS/VALUES)
```
but I recommend this bad boi:
```
manim <filename>.py (OPTIONAL_SCENE_INDEX_NUMBER/NAME) -pqh --fps 60
```
***NOTE:**
    - `-p` means preview/auto play when done the rendering process.
    - `-qh` stands for `--quality high`, means render in FullHD resolution `1920x1080`.
    - `--fps 60` I think I don't have to explain this.

## Installation
The easiest way of installing Manim and its dependencies is by using a package manager like `Chocolatey` or `Scoop`. If you are not afraid of editing your System’s PATH, a manual installation is also possible. In fact, if you already have an existing Python installation (3.7-3.10), it might be the easiest way to get everything up and running.

Manim requires a recent version of Python (3.7–3.10) and `ffmpeg` in order to work.

- Chocolatey: Manim can be installed via Chocolatey simply by running:
```
choco install manimce
```

- Scoop: While there is no recipe for installing Manim with Scoop directly, you can install all requirements by running:
```
scoop install python ffmpeg
```
and then Manim can be installed by running:
```
python -m pip install manim
```
Manim should now be installed on your system. Continue reading the optional dependencies section below.

## Optional Dependencies
- In order to make use of Manim’s interface to `LaTeX` to, for example, render equations, `LaTeX` has to be installed as well. Note that this is an optional dependency: if you don’t intend to use `LaTeX`, you don’t have to install it.
- For Windows, the recommended `LaTeX` distribution is [MiKTeX](https://miktex.org/download). You can install it by using the installer from the linked MiKTeX site, or by using the package manager of your choice.
```
Chocolatey: choco install miktex.install
Scoop: scoop install latex
```
- If you are concerned about disk space, there are some alternative, smaller distributions of `LaTeX`.
- Using Chocolatey: If you used Chocolatey to install manim or are already a chocolatey user, then you can simply run:
```
choco install manim-latex
```
It is a dedicated package for Manim based on `TinyTeX` which contains all the required packages that Manim interacts with.
- Manual Installation: You can also use TinyTeX:
```
Chocolatey: choco install tinytex
```
```
Scoop: first scoop bucket add r-bucket` #(https://github.com/cderv/r-bucket.git)
       scoop install tinytex
```
alternative installation instructions can be found at their website. Keep in mind that you will have to manage the `LaTeX` packages installed on your system yourself via `tlmgr`. Therefore we only recommend this option if you know what you are doing.
- The full list of `LaTeX` packages which Manim interacts with in some way (a subset might be sufficient for your particular application) are:
```
amsmath babel-english cbfonts-fd cm-super ctex doublestroke dvisvgm everysel
fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin
mathastext microtype ms physics preview ragged2e relsize rsfs
setspace standalone tipa wasy wasysym xcolor xetex xkeyval
```

## Available Scenes

| Scene Name | Link | Approximated Rendering Time |
| ------ | ------ | ------ |
| Pythagorean Theorem Proof | [Click Here](https://github.com/NooberrUwU/ManimRepository/tree/main/Pythagorean%20Theorem%20Proof) | Unknown |
| AM-GM Cauchy Inequality Proof | [Click Here](https://github.com/NooberrUwU/ManimRepository/tree/main/AM-GM%20Cauchy%20Inequality%20Proof) | 14m08s
