ꦥꦤ꧀ꦣꦸꦮꦤ꧀
===
Serat iki kanggo pandhuwan menawa sliramu arep kodhing Python nganggo aksara Jawa. Ana ing serat iki bakal dak udaraké kabèh fungsi-fungsi ana ing basa pamrograman Python kang wus kaalihaksaraaké ing aksara Jawa.

Sliramu bisa nulis angka nganggo aksara Latin, utawa aksara Jawa.
```python
0 = ꧐
1 = ꧑
2 = ꧒
3 = ꧓
4 = ꧔
5 = ꧕
6 = ꧖
7 = ꧗
8 = ꧘
9 = ꧙
```
# ꦲꦸꦏꦫ
Ing isor iki ukara utawa istilah ana ing `ꦱꦮ` lan padhanané ana ing `python`.
Ing kolom mburi dhéwé, dak sertaaké tulisan Latiné, menawa bisa nggampangaké. Cara Latin iku ora dianggo ana ing `ꦱꦮ`.
| Python  | ꦱꦮ | Latiné |
|---|---|----|
|  `True` |  `ꦧꦼꦤꦼꦂ` | bener |
|  `False` |  `ꦱꦭꦃ` | salah |
| `None`  |  `ꦱꦸꦮꦸꦁ` | suwung |
|  `as` |  `ꦢꦢꦶ` | dadi |
| `assert`  |  `ꦱꦶꦢ` | sida |
|  `async` |  `ꦲꦺꦴꦫꦩꦡꦸꦏ꧀` | ora mathuk |
|  `and` |  `ꦭꦤ꧀` | lan |
|  `await` |  `ꦤꦸꦁꦒꦸ` | nunggu |
| `break` | `ꦭꦺꦫꦺꦤ꧀` | lèrèn |
| `class` | `ꦏꦼꦭꦱ꧀` | kelas |
| `continue` | `ꦠꦼꦫꦸꦱ꧀ꦱꦏꦺ` | terusaké |
| `def` | `ꦥ꦳ꦸꦁꦱꦶ` | fungsi |
| `del` | `ꦧꦸꦱꦏ꧀` | busak |
| `elif` | `ꦲꦸꦠꦮꦭꦶꦪꦤꦺ` | utawa liyané |
| `else` | `ꦭꦶꦪꦤꦺ` | liyané |
| `except` | `ꦏꦼꦗꦧ` | kejaba |
| `finally` | `ꦫꦩ꧀ꦥꦸꦁꦔꦤ꧀` | rampungané |
| `for` | `ꦏꦁꦒꦺꦴ` | kanggo |
| `from` | `ꦱꦏ` | saka |
| `global` | `ꦗꦒꦢ꧀` | jagad |
| `if` | `ꦪꦺꦤ꧀` | yèn |
| `import` | `ꦗꦸꦥꦸꦏ꧀` | jupuk |
| `in` | `ꦲꦶꦁ` | ing |
| `is` | `ꦪꦲꦶꦏꦸ` | yaiku |
| `lambda` | `ꦧꦶꦪꦤ꧀ꦠꦸ` | biyantu |
| `not` | `ꦢꦸꦢꦸ` | dudu |
| `nonlocal` | `ꦲꦺꦴꦫꦭꦺꦴꦏꦭ꧀` | ora lokal |
| `or` | `ꦲꦸꦠꦮ` | utawa |
| `pass` | `ꦭꦶꦮꦠ꧀ꦠꦶ` | liwati |
| `raise` | `ꦲꦁꦏꦠ꧀` | angkat |
| `return` | `ꦧꦭꦶꦏ꧀` | balik |
| `try` | `ꦕꦺꦴꦧ` | coba |
| `while` | `ꦱꦮꦼꦠꦮꦶꦱ꧀` | sawetawis |
| `with` | `ꦏꦫꦺꦴ` | karo |
| `yield` | `ꦏꦫꦺꦴ` | kasil |
| `bool` | `ꦭꦺꦴꦒꦶꦱ꧀` | logis |
| `int` | `ꦲꦁꦏ` | angka |
| `float` | `ꦣꦺꦱꦶꦩꦭ꧀` | dhèsimal |
| `string` | `ꦲꦸꦏꦫ` | ukara |
|`__dict__`| `__ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀__` | `__objèk__` |


#
# ꦥ꦳ꦸꦁꦱꦶ (fungsi)

## ꦩꦸꦠ꧀ꦭꦏ꧀

Fungsi iki padha déné karo fungsi `abs` ana ing `python`. Fungsi iki bakal mbalèkaké nilai absolut.
```python
ꦲ  = ꦩꦸꦠ꧀ꦭꦏ꧀(-꧗.꧒꧕)

# bisa uga ditulis
# ꦲ  = ꦩꦸꦠ꧀ꦭꦏ꧀(-7.25)

ꦥꦿꦶꦤ꧀(ꦲ)
```
Output:
```bash
꧗.꧒꧕
```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦧꦱ.ꦱꦮ)

## ꦲꦥꦸꦱ꧀ꦲꦠꦿꦶꦧꦸꦠ꧀

Fungsi iki padha déné karo fungsi `delattr` ana ing python. Fungsi iki kanggo mbusak atribut saka objèk.
```python
ꦏꦼꦭꦱ꧀ ꦩꦤꦸꦁꦱ:
    ꦥ꦳ꦸꦁꦱꦶ __ꦊꦏꦱ꧀__(ꦣꦺꦮꦺ):
        ꦣꦺꦮꦺ.ꦲꦫꦤꦺ = "ꦥꦲꦶꦗꦺꦴ"
        ꦣꦺꦮꦺ.ꦲꦸꦩꦸꦂ = 36 # utawa ꧓꧖
        ꦣꦺꦮꦺ.ꦤꦒꦫ = "ꦆꦤ꧀ꦝꦺꦴꦤꦺꦱꦶꦪ"

ꦩ = ꦩꦤꦸꦁꦱ()
ꦥꦿꦶꦤ꧀(ꦩ.__ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀__)

ꦲꦥꦸꦱ꧀ꦲꦠꦿꦶꦧꦸꦠ꧀(ꦩ, 'ꦲꦸꦩꦸꦂ')

ꦥꦿꦶꦤ꧀(ꦩ.__ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀__)

```
Output:
```bash
{'ꦲꦫꦤꦺ': 'ꦥꦲꦶꦗꦺꦴ', 'ꦲꦸꦩꦸꦂ': ꧓꧖, 'ꦤꦒꦫ': 'ꦆꦤ꧀ꦝꦺꦴꦤꦺꦱꦶꦪ'}
{'ꦲꦫꦤꦺ': 'ꦥꦲꦶꦗꦺꦴ', 'ꦤꦒꦫ': 'ꦆꦤ꧀ꦝꦺꦴꦤꦺꦱꦶꦪ'}

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦏꦭꦱ.ꦱꦮ)

## ꦕꦩ꧀ꦥꦸꦂ

Fungsi iki padha karo fungsi `hash` ana ing `python`.

```python
# ꦕꦩ꧀ꦥꦸꦂ kanggo integer (angka bulet), ora owah
ꦥꦿꦶꦤ꧀("ꦕꦩ꧀ꦥꦸꦂ kanggo ꧑꧘ yaiku: ", ꦕꦩ꧀ꦥꦸꦂ(꧑꧘) )

# ꦕꦩ꧀ꦥꦸꦂ kanggo dhèsimal
ꦥꦿꦶꦤ꧀("ꦕꦩ꧀ꦥꦸꦂ kanggo ꧑꧘꧑.꧒꧓ yaiku: ", ꦕꦩ꧀ꦥꦸꦂ(꧑꧘꧑.꧒꧓) )

# ꦕꦩ꧀ꦥꦸꦂ kanggo string (aksara wyanjana)
ꦥꦿꦶꦤ꧀("ꦕꦩ꧀ꦥꦸꦂ kanggo ꦥꦶꦠꦺꦴꦤ꧀ yaiku: ", ꦕꦩ꧀ꦥꦸꦂ("ꦥꦶꦠꦺꦴꦤ꧀") )

```
Output:
```bash
ꦕꦩ꧀ꦥꦸꦂ kanggo ꧑꧘ yaiku: ꧑꧘
ꦕꦩ꧀ꦥꦸꦂ kanggo ꧑꧘꧑.꧒꧓ yaiku: ꧕꧓꧐꧓꧔꧓꧘꧙꧒꧑꧑꧙꧑꧒꧖꧑꧙꧗
ꦕꦩ꧀ꦥꦸꦂ kanggo ꦥꦶꦠꦺꦴꦤ꧀ yaiku: -꧗꧔꧘꧖꧓꧗꧙꧘꧙꧐꧖꧐꧑꧔꧐꧘꧘꧒꧓

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦱ.ꦱꦮ)

## ꦱꦏ꧀ꦭꦺꦧꦠ꧀

Fungsi iki padha karo `memoryview` ing `python`. Kegunaané mbalèkaké _memory view_ saka objèk.
Fungsi iki amung nampa bytes, kamangka aksara Jawa iku dudu karakter ascii, mula kudu diowahi dhisik dadi byte nganggo fungsi [ꦧꦪ꧀ꦠ](#ꦧꦪ꧀ꦠ).

```python
ꦧꦠ = ꦧꦪ꧀ꦠ("ꦱꦸꦒꦼꦁ", "utf-8")
ꦩ = ꦱꦏ꧀ꦭꦺꦧꦠ꧀(ꦧꦠ)

ꦥꦿꦶꦤ꧀(ꦩ)

# mbalèkaké yunikod saka aksara sepisan
ꦥꦿꦶꦤ꧀(ꦩ[꧐])


# mbalèkaké yunikod saka aksara kapindho
ꦥꦿꦶꦤ꧀(ꦩ[꧑])

```
Output:
```bash
<memory at ꧐x꧑꧐꧔꧐d꧖꧔c꧐>
꧒꧓꧔
꧑꧖꧖
```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦩꦩꦫ.ꦱꦮ)

## ꦲꦺꦴꦩ꧀ꦧꦾꦺꦴꦏ꧀

Fungsi iki padha karo `set` ing `python`. Kegunaané kanggo gawé kumpulan objèk.

```python
ꦩ = ꦲꦺꦴꦩ꧀ꦧꦾꦺꦴꦏ꧀(("ꦣꦸꦏꦸ","ꦣꦺꦴꦚ꧀ꦣꦺꦴꦁ","ꦱꦭꦏ꧀"))

ꦥꦿꦶꦤ꧀(ꦩ)

```
Output:
```bash
{'ꦱꦭꦏ꧀', 'ꦣꦺꦴꦚ꧀ꦣꦺꦴꦁ', 'ꦣꦸꦏꦸ'}
```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦱꦠ.ꦱꦮ)


## ꦏꦧꦺꦃ
Fungsi iki padha karo `all` ing `python`. Fungsi iki bakal mbalèkaké `ꦧꦼꦤꦼꦂ` yèn kabèh ukara isiné ꦧꦼꦤꦼꦂ (_True_), lan bakal mbalèkaké `ꦱꦭꦃ` yèn ora.

```python
ꦩ = [ꦧꦼꦤꦼꦂ,ꦧꦼꦤꦼꦂ,ꦧꦼꦤꦼꦂ]
ꦏ = ꦏꦧꦺꦃ(ꦩ)

ꦥꦿꦶꦤ꧀("iki bakal asilé ꦧꦼꦤꦼꦂ (True)")
ꦥꦿꦶꦤ꧀(ꦏ)

ꦩ = [ꦧꦼꦤꦼꦂ,ꦧꦼꦤꦼꦂ,ꦱꦭꦃ]
ꦏ = ꦏꦧꦺꦃ(ꦩ)

ꦥꦿꦶꦤ꧀("iki bakal asilé ꦱꦭꦃ (False)")
ꦥꦿꦶꦤ꧀(ꦏ)


```
Output:
```bash
iki bakal asilé ꦧꦼꦤꦼꦂ (True)
True
iki bakal asilé ꦱꦭꦃ (False)
False
```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦭꦭ.ꦱꦮ)

## ꦧꦲꦸꦱꦱ꧀ꦠꦿ
Fungsi iki padha karo `dict` ing `python`. Fungsi iki kanggo gawé kolèksi sing ora kudu urut, bisa diowahi lan ana indhèksé.

```python
ꦩ = ꦧꦲꦸꦱꦱ꧀ꦠꦿ(ꦗꦼꦤꦼꦁ = "ꦱꦸꦢꦂꦩꦗꦶ", ꦲꦸꦩꦸꦂ = "꧒꧓", ꦤꦼꦒꦫ = "ꦩꦠꦫꦩ꧀")

ꦥꦿꦶꦤ꧀(ꦩ)


```
Output:
```bash
{'ꦗꦼꦤꦼꦁ': 'ꦱꦸꦢꦂꦩꦗꦶ', 'ꦲꦸꦩꦸꦂ': '꧒꧓', 'ꦤꦼꦒꦫ': 'ꦩꦠꦫꦩ꧀'}
```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦢꦏ.ꦱꦮ)

## ꦥꦶꦠꦸꦭꦸꦁ 
Fungsi iki padha karo `help` ing `python`. Fungsi iki kanggo ngetokné _help_ utawa pitulung ana ing sistem _built-in_ `python`.
Yèn diceluk kosongan, bakal metu pandhuan interaktif, ananging yèn diwènèhi jeneng salah siji fungsi, mula bakal diwènèhi pandhuan angenani bab iku.
Fungsi sing bisa diceluk ana ing kéné, isih kudu padha karo fungsi asliné `python`, dadi yèn arep ndelok pitulung kanggo fungsi `ꦥꦿꦶꦤ꧀` nulisé kudu tetep `print`.

```python
ꦥꦶꦠꦸꦭꦸꦁ(print)

```
_sing iki cobanen dhéwé ya, dawa soalé._

## ꦩꦶꦤꦶꦩꦭ꧀
Fungsi iki padha karo `min` ana ing `python`. Kegunaané kanggo njupuk sing bijiné paling cendhek. Yèn isiané iku _string_ utawa _ukara_, mula bakal diurutaké miturut abjad.

```python
ꦩ = ꦩꦶꦤꦶꦩꦭ꧀(꧓, ꧖, ꧒)

ꦥꦿꦶꦤ꧀(ꦩ)


```
Output:
```bash
꧒

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦩꦤ.ꦱꦮ)

## ꦒꦺꦠꦂ 
Fungsi iki padhanané `getattr` ana ing `python`. Kegunaané kanggo njupuk biji saka atribut tartamtu ana ing sawijining objèk.
```python
ꦏꦼꦭꦱ꧀ ꦩꦤꦸꦁꦱ:
    ꦲꦫꦤꦺ = "ꦥꦲꦶꦗꦺꦴ"
    ꦲꦸꦩꦸꦂ = 36 # utawa ꧓꧖
    ꦤꦒꦫ = "ꦆꦤ꧀ꦝꦺꦴꦤꦺꦱꦶꦪ"

ꦏ = ꦒꦺꦠꦂ(ꦩꦤꦸꦁꦱ, 'ꦲꦸꦩꦸꦂ')

ꦥꦿꦶꦤ꧀(ꦏ)

```
Output:
```bash
꧓꧖

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦒꦠꦫ.ꦱꦮ)

## ꦱꦺꦠꦂ
Fungsi iki padhanané `setattr` ana ing `python`. Kegunaané kanggo ngisi biji utawa _value_ saka atribut tartamtu ana ing sawijining objèk.

```python
ꦏꦼꦭꦱ꧀ ꦩꦤꦸꦁꦱ:
    ꦲꦫꦤꦺ = "ꦥꦲꦶꦗꦺꦴ"
    ꦲꦸꦩꦸꦂ = 36 # utawa ꧓꧖
    ꦤꦒꦫ = "ꦆꦤ꧀ꦝꦺꦴꦤꦺꦱꦶꦪ"

ꦱꦺꦠꦂ(ꦩꦤꦸꦁꦱ, 'ꦲꦸꦩꦸꦂ', ꧔꧕ )

ꦏ = ꦒꦺꦠꦂ(ꦩꦤꦸꦁꦱ, 'ꦲꦸꦩꦸꦂ')

ꦥꦿꦶꦤ꧀(ꦏ)

```
Output:
```bash
꧔꧕

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦱꦠ.ꦱꦮ)

## ꦏꦁ
Fungsi iki padhanané `any` ana ing `python`. Fungsi iki bakal ngetokaké nilai `True` menawa ana nilai `True` sak jroning `ꦥꦿꦠꦺꦭꦤ꧀`.

```python
ꦩ = [ꦱꦭꦃ, ꦧꦼꦤꦼꦂ, ꦱꦭꦃ]

ꦏ = ꦏꦁ(ꦩ)

ꦥꦿꦶꦤ꧀(ꦏ)

```
Output:
```bash
True

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦤ.ꦱꦮ)

## ꦣꦶꦂ
Fungsi iki padhanané `dir` ana ing `python`. Fungsi iki bakal mbalèkaké samubarang prabotan lan cara ana ing salah sawijining objèk.

```python
ꦏꦼꦭꦱ꧀ ꦩꦤꦸꦁꦱ:
    ꦲꦫꦤꦺ = "ꦥꦲꦶꦗꦺꦴ"
    ꦲꦸꦩꦸꦂ = 36 # utawa ꧓꧖
    ꦤꦒꦫ = "ꦆꦤ꧀ꦝꦺꦴꦤꦺꦱꦶꦪ"

ꦥꦿꦶꦤ꧀(ꦣꦶꦂ(ꦩꦤꦸꦁꦱ))

```
Output:
```bash
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ꦤꦒꦫ', 'ꦲꦫꦤꦺ', 'ꦲꦸꦩꦸꦂ']

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦢꦫ.ꦱꦮ)

## ꦲꦺꦏ꦳꧀
Fungsi kang padha karo `hex` ana ing `python`. Fungsi iki kanggo ngubah angka dadi heksadesimal.
```python
ꦲ = ꦲꦺꦏ꦳꧀(꧒꧕꧕)

ꦥꦿꦶꦤ꧀(ꦲ)

```
Output:
```bash
꧐xff

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦏꦱ.ꦱꦮ)

## ꦧꦕꦸꦠ꧀
Fungsi padhanané `next` ana ing `python`. Kanggo njupuk nilai sak banjuré saka pratèlan tartamtu.

```python
ꦩꦭꦱ = ꦥꦫ(["ꦣꦺꦴꦚ꧀ꦣꦺꦴꦁ", "ꦱꦭꦏ꧀", "ꦣꦸꦏꦸ"])
ꦏ = ꦧꦕꦸꦠ꧀(ꦩꦭꦱ)
ꦥꦿꦶꦤ꧀(ꦏ)
ꦏ = ꦧꦕꦸꦠ꧀(ꦩꦭꦱ)
ꦥꦿꦶꦤ꧀(ꦏ)
ꦏ = ꦧꦕꦸꦠ꧀(ꦩꦭꦱ)
ꦥꦿꦶꦤ꧀(ꦏ)


```
Output:
```bash
ꦣꦺꦴꦚ꧀ꦣꦺꦴꦁ
ꦱꦭꦏ꧀
ꦣꦸꦏꦸ

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦤꦏꦱ.ꦱꦮ)

## ꦲꦶꦫꦶꦱ꧀ꦱꦤ꧀
Fungsi iki padha karo `slice` ana ing `python`. Fungsi iki kanggo motong bagian saka pratèlan.

```python
ꦲ = ("ꦲ", "ꦤ", "ꦕ", "ꦫ", "ꦏ", "ꦢ", "ꦠ", "ꦱ", "ꦮ", "ꦭ")
ꦏ = ꦲꦶꦫꦶꦱ꧀ꦱꦤ꧀(꧓)
ꦥꦿꦶꦤ꧀(ꦲ[ꦏ])
```
Output:
```bash
('ꦲ', 'ꦤ', 'ꦕ')

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦱꦭꦕ.ꦱꦮ)

## ꦲꦱ꧀ꦏꦶ
Fungsi iki padha karo `ascii` ana ing `python`. Kanggo mbalèkaké hasil kang gampang diwaca saka manéka objèk. Fungsi iki bakal ngganti aksara _non-ascii_ dadi aksara uwal (_escape_). Amerga aksara jawa kalebu aksara non-ascii, mula yèn dikenani fungsi iki bakal dadi aksara uwal kabèh, sahingga kanggo conto dipilih aksara latin supaya kétok.

```python
ꦏ = ꦲꦱ꧀ꦏꦶ("nami kula Ståle")
ꦥꦿꦶꦤ꧀(ꦏ)
```
Output:
```bash
'nami kula St\xe꧕le'

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦱꦏ.ꦱꦮ)

## ꦣꦶꦥ꦳꧀ꦩꦺꦴꦢ꧀
Fungsi iki padhanané `divmod` ana ing `python`. Fungsi iki bakal mbalèkaké nilai _tuple_ kang isiné yaiku nilai para lan sisané nalika argumèn siji dipara argumèn loro.

```python
ꦏ = ꦣꦶꦥ꦳꧀ꦩꦺꦴꦢ꧀(꧕,꧒)
ꦥꦿꦶꦤ꧀(ꦏ)
```
Output:
```bash
(꧒, ꧑)

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦣꦉꦩꦢ.ꦱꦮ)

## ꦲꦶꦣꦶ
Fungsi iki padhanané `id` ana ing `python`. Kegunaané kanggo mbalèkaké _unique id_ saka sawijining objèk.

```python
ꦏ = ("ꦣꦺꦴꦚ꧀ꦣꦺꦴꦁ", "ꦱꦭꦏ꧀", "ꦣꦸꦏꦸ")
ꦪ = ꦲꦶꦣꦶ(ꦏ)
ꦥꦿꦶꦤ꧀(ꦪ)
```
Output:
```bash
꧔꧕꧕꧙꧔꧗꧒꧙꧖꧐

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦣ.ꦱꦮ)

## ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀
Fungsi iki padha déné karo `object` ana ing `python`. Kegunaané kanggo mbalèkaké objèk kosong.

```python
ꦏ = ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀()
ꦥꦿꦶꦤ꧀(ꦣꦶꦂ(ꦏ))
```
Output:
```bash
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦧꦗꦏ.ꦱꦮ)

## ꦲꦸꦫꦸꦠ꧀
Fungsi iki padhanané `sorted` ana ing `python`. Kegunaané kanggo ngurutaké pratèlan.
_supaya kétok, dipilih conto nganggo aksara latin_

```python
ꦏ = ("a","c","e","b","f","d")
ꦪ = ꦲꦸꦫꦸꦠ꧀(ꦏ)
ꦥꦿꦶꦤ꧀(ꦪ)
```
Output:
```bash
['a', 'b', 'c', 'd', 'e', 'f']

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦱꦫꦠ.ꦱꦮ)

## ꦧꦶꦤ꧀
Fungsi iki padhanané `bin` ana ing `python`. Kegunaané kanggo ngubah angka (_integer_) dadi ukara binari.

```python
ꦏ = ꧑꧐
ꦥꦿꦶꦤ꧀("ꦲꦱꦭ꧀ꦭꦺ ",ꦏ)
ꦪ = ꦧꦶꦤ꧀(ꦏ)
ꦥꦿꦶꦤ꧀("ꦧꦶꦤꦫꦶꦤꦺ꧇ ",ꦪ)

ꦏ = 10
ꦥꦿꦶꦤ꧀("ꦲꦱꦭ꧀ꦭꦺ ",ꦏ)
ꦪ = ꦧꦶꦤ꧀(ꦏ)
ꦥꦿꦶꦤ꧀("ꦧꦶꦤꦫꦶꦤꦺ꧇ ",ꦪ)

```
Output:
```bash
ꦲꦱꦭ꧀ꦭꦺ ꧑꧐
ꦧꦶꦤꦫꦶꦤꦺ ꧐b꧑꧐꧑꧐
ꦲꦱꦭ꧀ꦭꦺ ꧑꧐
ꦧꦶꦤꦫꦶꦤꦺ ꧐b꧑꧐꧑꧐

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦧꦤꦫ.ꦱꦮ)

## ꦲꦺꦤꦸꦩꦼꦂꦫꦺꦠ꧀
Fungsi iki padha karo `enumerate` ana ing `python`. Fungsi iki bakal nambahaké urutan itungan dadi _key_ ana ing pratèlan kang di _enumerate_.

```python
ꦏ = ("ꦣꦸꦏꦸ","ꦣꦺꦴꦚ꧀ꦣꦺꦴꦁ","ꦱꦭꦏ꧀")
ꦪ = ꦲꦺꦤꦸꦩꦼꦂꦫꦺꦠ꧀(ꦏ)
ꦥꦿꦶꦤ꧀(ꦥꦿꦠꦺꦭꦤ꧀(ꦪ))


```
Output:
```bash
[(꧐, 'ꦣꦸꦏꦸ'), (꧑, 'ꦣꦺꦴꦚ꧀ꦣꦺꦴꦁ'), (꧒, 'ꦱꦭꦏ꧀')]

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦤꦩꦫꦠ.ꦱꦮ)

## ꦠꦸꦭꦶꦱ꧀
Fungsi iki padha karo `input` ana ing `python`. Fungsiné kanggo ngolèhaké nulis.

```python
ꦥꦿꦶꦤ꧀("ꦠꦸꦭꦶꦱ꧀ꦱꦗꦼꦤꦼꦁꦩꦸ:")

ꦏ = ꦠꦸꦭꦶꦱ꧀()

ꦥꦿꦶꦤ꧀("ꦱꦸꦒꦼꦁꦱꦶꦪꦁ "+ ꦏ)



```
Output:
```bash
ꦠꦸꦭꦶꦱ꧀ꦱꦗꦼꦤꦼꦁꦩꦸ:
lantip
ꦱꦸꦒꦼꦁꦱꦶꦪꦁ lantip

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦤꦥꦠ.ꦱꦮ)

## ꦲꦺꦴꦏ꧀ꦠ
Fungsi iki padhanané `oct` ana ing `python`. Kegunaané kanggo ngowahi _integer_ (angka) dadi ukara oktal.

```python
ꦏ = ꦲꦺꦴꦏ꧀ꦠ(꧒꧓)

ꦥꦿꦶꦤ꧀(ꦏ)



```
Output:
```bash
꧐o꧒꧗

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦕꦠ.ꦱꦮ)

## ꦱꦶꦒꦼꦒ꧀
Fungsi iki padhanané `staticmethod` ana ing `python`. Kegunaané kanggo mbalèkaké mètodhe statik saka sawijining fungsi. Fungsi iki dianggep kurang `pythonic`, mula ing `python` versi saiki, digawe `decorator` kanthi aran padha `@staticmethod`.

```python
ꦏꦼꦭꦱ꧀ ꦩꦠꦶꦏ:
    ꦥ꦳ꦸꦁꦱꦶ ꦠꦩ꧀ꦧꦃ(ꦏ, ꦪ):
        ꦧꦭꦶꦏ꧀ ꦏ + ꦪ

# gawe mètodhe statik ꦠꦩ꧀ꦧꦃ
ꦩꦠꦶꦏ.ꦠꦩ꧀ꦧꦃ = ꦱꦶꦒꦼꦒ꧀(ꦩꦠꦶꦏ.ꦠꦩ꧀ꦧꦃ)

ꦥꦿꦶꦤ꧀('ꦗꦸꦩ꧀ꦭꦃꦲꦺ ꦪꦲꦶꦏꦸ :', ꦩꦠꦶꦏ.ꦠꦩ꧀ꦧꦃ(꧖, ꧘))



```
Output:
```bash
ꦗꦸꦩ꧀ꦭꦃꦲꦺ ꦪꦲꦶꦏꦸ :꧑꧔

```
> Conto iki bisa didelok ana ing [kéné](./examples/ꦱꦠꦠꦩꦠꦢ.ꦱꦮ)

## ꦭꦺꦴꦒꦶꦱ꧀
Fungsi iki padhanané `bool` ana ing `python`. Bakal ngetokaké nilai _boolean_ saka sawijining objèk.

```python
ꦏ = ꦭꦺꦴꦒꦶꦱ꧀(꧑)

ꦥꦿꦶꦤ꧀(ꦏ)



```
Output:
```bash
True

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦧꦲꦲꦭ.ꦱꦮ)


## ꦲꦺꦥ꦳ꦭ꧀
Fungsi iki padhanané `eval` ana ing `python`. Kegunaané kanggo niliki menawa ukara tartamtu iku kegolong ukara python apa dudu, yèn iya, bakal dilakokaké.

```python
ꦏ = 'ꦥꦿꦶꦤ꧀(35)'

ꦲꦺꦥ꦳ꦭ꧀(ꦏ)


```
Output:
```bash
꧓꧕

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦥꦭ.ꦱꦮ)


## ꦲꦁꦏ
Fungsi iki padhanané `int` ana ing `python`. Kegunaané kanggo ngowahi dadi angka wutuh.

```python
ꦏ = ꦲꦁꦏ(꧔꧉꧕) #utawa ꦲꦁꦏ(4.5)

ꦥꦿꦶꦤ꧀(ꦏ)


```
Output:
```bash
꧔

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦤꦠ.ꦱꦮ)


## ꦧꦸꦏꦏ꧀
Fungsi iki padhanané `open` ana ing `python`. Kegunaané kanggo mbukak sawijining fail banjur didadèkaké objèk.

```python
ꦏ = ꦧꦸꦏꦏ꧀("file_conto_open.txt","r") 

ꦥꦿꦶꦤ꧀(ꦏ.read())


```
Output:
```bash
ꦥꦸꦤꦶꦏꦏꦮꦿꦸꦃꦥꦼꦥꦏ꧀ꦧꦱꦱꦮ꧉
ꦮꦺꦴꦚ꧀ꦠꦼꦤ꧀ꦲꦶꦁꦩꦿꦶꦏꦶꦏꦛꦃꦕꦺꦴꦚ꧀ꦠꦺꦴꦏꦒꦼꦩ꧀ꦱꦶꦤꦲꦸꦧꦱꦱꦮ꧉


```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦥꦤ.ꦱꦮ)

## ꦱꦼꦫꦠ꧀
Fungsi iki padhanané fungsi `str` ana ing `python`. Kanggo ngowahi angka dadi ukara utawa _string_.


```python
ꦏ = ꦱꦼꦫꦠ꧀(꧔꧉꧕) #utawa ꦱꦼꦫꦠ꧀(4.5)

ꦥꦿꦶꦤ꧀(ꦏ)


```
Output:
```bash
꧔.꧕


```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦱꦠꦫꦒ.ꦱꦮ)

## ꦊꦏꦱ꧀ꦩꦤꦺꦃ
Fungsi iki padha déné karo fungsi `breakpoint` ana ing `pyhton`. Fungsi iki lagi ana ing `python 3.7`, kegunaané kanggo métani tuma utawa _debugging_. Nggunakaké fungsi iki, bakal gampang banget yèn dibandingaké nganggo _debugger_ liyané kayata `pdb` utawa `web-pdb`.

```python
ꦏ = []
ꦏꦁꦒꦺꦴ ꦲ ꦲꦶꦁ ꦲꦤ꧀ꦠꦫ(꧕):
    ꦏ.append(ꦲ)
    ꦪꦺꦤ꧀ ꦲ == ꧔:
        ꦊꦏꦱ꧀ꦩꦤꦺꦃ()
        
ꦥꦿꦶꦤ꧀(ꦏ)


```
Output:
```bash
-> for ꦲ in range(5):
(Pdb) c
[꧐, ꧑, ꧒, ꧓, ꧔]

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦧꦫꦏꦥꦤꦠ.ꦱꦮ)

## ꦲꦗꦂ
Fungsi iki padhanané fungsi `exec` ana ing `python`. Kegunaané yaiku kanggo èksekusi dinamis ing _program_ `python`.


```python
ꦏ = "ꦥꦿꦶꦤ꧀('ꦗꦗꦭꦶꦲꦶꦏꦶꦥꦫꦺꦚ꧀ꦠꦃꦲꦗꦂ')"
  
ꦲꦗꦂ(ꦏ)


```
Output:
```bash
ꦗꦗꦭꦶꦲꦶꦏꦶꦥꦫꦺꦚ꧀ꦠꦃꦲꦗꦂ

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦏꦱꦏ.ꦱꦮ)

## ꦧꦭꦤꦺ
Fungsi iki padha déné karo fungsi `isinstance` ana ing `python`. Fungsi iki bakal mbalèkaké `True` utawa `False` yèn salah sawijining objèk kalebu tipe utawa jinis saka tipe kang wus disamadyaaké.


```python
ꦏ = ꦧꦭꦤꦺ(꧕, ꦲꦁꦏ)
  
ꦥꦿꦶꦤ꧀(ꦏ)


```
Output:
```bash
True

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦏꦱꦫ.ꦱꦮ)

## ꦲꦺꦴꦫꦼꦢ꧀
Fungsi iki padhanané fungsi `ord` ana ing `python`. Fungsi iki bakal mbalèkaké angka saka sawijining karakter.


```python
ꦏ = ꦲꦺꦴꦫꦼꦢ꧀("ꦏ")
  
ꦥꦿꦶꦤ꧀(ꦏ)


```
Output:
```bash
꧔꧓꧔꧐꧗

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦫꦢ.ꦱꦮ)


## ꦗꦸꦩ꧀ꦭꦃ
Fungsi iki padha déné karo fungsi `sum` ana ing `python`. Kegunaané kanggo ngétung jumlah saka sawijing _tuple_ utawa _list_.

```python
ꦏ = (꧑,꧒,꧓,꧔)

ꦪ = ꦗꦸꦩ꧀ꦭꦃ(ꦏ)

ꦥꦿꦶꦤ꧀(ꦪ)


```
Output:
```bash
꧑꧐

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦱꦩ.ꦱꦮ)

## ꦧꦶꦠꦼꦫꦺ
Fungsi iki padha déné karo fungsi `bytearray` ana ing `python`. Kegunaané kanggo ngasilaké _bytearray_ saka sawijining objèk.

```python
ꦏ = ꦧꦶꦠꦼꦫꦺ(꧓)

ꦥꦿꦶꦤ꧀(ꦏ)


```
Output:
```bash
bytearray(b'\x꧐꧐\x꧐꧐\x꧐꧐')

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦧꦠꦲꦫ.ꦱꦮ)

## ꦥ꦳ꦶꦭ꧀ꦠꦼꦂ
Fungsi iki padhanané `filter` ana ing `python`. Fungsi iki bakal ngasilaké _iterator_ sing bagéan-bagéané disaring nganggo fungsi liya, kanggo ngetès yen bagéan iku bisa ditampa apa ora.

```python
ꦲꦸꦩꦸꦂ = [꧕꧈꧘꧈꧑꧗꧈꧑꧙]

ꦥ꦳ꦸꦁꦱꦶ ꦉꦸꦁꦱꦶꦏꦸ(ꦏ):
    ꦪꦺꦤ꧀ ꦏ < ꧑꧘:
        ꦧꦭꦶꦏ꧀ ꦱꦭꦃ
    ꦭꦶꦪꦤꦺ:
        ꦧꦭꦶꦏ꧀ ꦧꦼꦤꦼꦂ

ꦢꦺꦮꦱ = ꦥ꦳ꦶꦭ꧀ꦠꦼꦂ(ꦉꦸꦁꦱꦶꦏꦸ, ꦲꦸꦩꦸꦂ)

ꦏꦁꦒꦺꦴ ꦏ ꦲꦶꦁ ꦢꦺꦮꦱ:
    ꦥꦿꦶꦤ꧀(ꦏ)


```
Output:
```bash
꧑꧙

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦥꦭꦠꦫ.ꦱꦮ)

## ꦲꦤ꧀ꦣꦃꦲꦤ꧀
Fungsi iki padhanané fungsi `issubclass` ana ing `python`. Fungsi iki bakal mbalèkaké hasil `True`, yen objèk kang ditemtokaké iku kalebu _subclass_ saka sawijing objèk.

```python
ꦏꦼꦭꦱ꧀ ꦲꦸꦩꦸꦂꦏꦸ:
    ꦲꦸꦩꦸꦂ = ꧓꧕

ꦏꦼꦭꦱ꧀ ꦒꦮꦺꦪꦤ꧀ꦏꦸ(ꦲꦸꦩꦸꦂꦏꦸ):
    ꦗꦼꦤꦼꦁ = "ꦥꦲꦶꦗꦺꦴ"
    ꦲꦸꦩꦸꦂ = ꦲꦸꦩꦸꦂꦏꦸ

ꦏ = ꦲꦤ꧀ꦣꦃꦲꦤ꧀(ꦒꦮꦺꦪꦤ꧀ꦏꦸ, ꦲꦸꦩꦸꦂꦏꦸ)

ꦥꦿꦶꦤ꧀(ꦏ)

```
Output:
```bash
True

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦲꦱꦏꦭꦧꦱ.ꦱꦮ)


## ꦏ꧀ꦮꦱ
Fungsi iki padhadéné karo `pow` ana ing `python`. Kegunaané kanggo ngasilaké nilai saka x pangkat y.

```python

ꦏ = ꦏ꧀ꦮꦱ(꧔,꧓)

ꦥꦿꦶꦤ꧀(ꦏ)

```
Output:
```bash
꧖꧔

```

> Conto iki bisa didelok ana ing [kéné](./examples/ꦥꦮ.ꦱꦮ)

## "ꦲꦸꦠꦩ": "super", #utama
## "ꦧꦪ꧀ꦠ": "bytes", #bayta
## "ꦣꦺꦱꦶꦩꦭ꧀": "float", #dhèsimal
## "ꦥꦫ": "iter", # para
## "ꦠꦸꦥꦼꦭ꧀": "tuple", # tupel
## "ꦔꦸꦚ꧀ꦢꦁ": "callable", # ngundang
## "ꦮꦸꦗꦸꦢ꧀": "format", # wujud
## "ꦢꦮ": "len", # dawa
## "ꦏꦒꦸꦁꦔꦤꦺ": "property", # kagungané
## "ꦩꦺꦴꦣꦺꦭ꧀": "type", # modhèl
## "ꦕꦂ": "chr", #car
## "ꦧꦼꦏꦸꦮꦤ꧀": "frozenset", #bekuwan
## "ꦥꦿꦠꦺꦭꦤ꧀": "list", #pratélan
## "ꦲꦤ꧀ꦠꦫ": "range", # antara
## "ꦥ꦳ꦉꦱ꧀": "vars", # fares
## "ꦩꦺꦠꦺꦴꦢ꧀ꦏꦼꦭꦱ꧀": "classmethod", #metodkelas
## "ꦗꦸꦥꦸꦏ꧀ꦲꦠꦼꦂ": "getattr", #jupuk ater
## "ꦥꦿꦶꦧꦸꦩꦶ": "locals", #pribumi
## "ꦫꦺꦥꦼꦂ": "repr", #reper
## "ꦗꦶꦥ꧀": "zip", #jip
## "ꦏꦺꦴꦩ꧀ꦥꦺꦭ꧀": "compile", #kompel
## "ꦱꦗꦒꦢ꧀": "globals", #sajagad
## "ꦥꦼꦠ": "map", #peta
## "ꦮꦭꦶꦏ꧀ꦲꦤꦺ": "reversed", #walikane
## "__ꦗꦸꦥꦸꦏ꧀__": "__import__", # __jupuk__
## "ꦩꦤꦺꦏ": "complex", #maneka
## "ꦒꦣꦃ": "hasattr", #gadhah
## "ꦥꦺꦴꦭ꧀": "max", #pol
## "ꦮꦸꦠꦸꦃ": "round", #wutuh