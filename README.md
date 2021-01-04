# epic
**epic** (**E**rror **P**ropagat**I**on **C**alculator) belirsizliğin yayılması işlemleri için kullanılabilecek bir modüldür.

Bu modül bu sayfada anlatılan yöntemi kullanır: https://math.stackexchange.com/a/1897743/482709

## Motivasyon
Bu modül [Astro Kod](https://www.youtube.com/channel/UC0A7Cv8ZTPw4hnukLbMcU6g) eğitim videoları için hazırlanmıştır. 

Bu modül pip ile kurulabilir hale getirilecektir.

Videolar:
- [Video 1](https://www.youtube.com/watch?v=APblJAr_4jg)
- [Video 2](https://www.youtube.com/watch?v=jvMkYr1PzdI)
- [Video 3](https://www.youtube.com/watch?v=Oh5lnm9J9qQ)

## Hakkında
Bu modül türev hesabı için [SymPy](https://www.sympy.org/en/index.html) kullanır.

## Kurulum
**epic** şmdilik pip ile kurulabilir değil. Ama en yakın zamanda olacaktır.

Şimdilik, epic paket dizinini gerekli yere kopyalayıp kullanabilirsiniz.

Yakında:

`pip install epic`

## Yetenekler
**epic** aşağıdaki işlemler için SymPy kullanır:

<img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;A&space;=&space;a&space;\pm&space;\delta&space;a&space;\newline&space;\newline&space;~~~~~B&space;=&space;b&space;\pm&space;\delta&space;b&space;\newline&space;\newline&space;~~~~~y&space;=&space;f(A,&space;B,&space;...)&space;\newline&space;\newline&space;~~~~~\delta&space;y&space;=&space;\sqrt{(\frac{\partial&space;f}{\partial&space;a}&space;\delta&space;a)^2&space;&plus;&space;(\frac{\partial&space;f}{\partial&space;b}&space;\delta&space;b)^2&space;&plus;&space;...}" title="A = a \pm \delta a \newline \newline ~~~~~B = b \pm \delta b \newline \newline ~~~~~y = f(A, B, ...) \newline \newline ~~~~~\delta y = \sqrt{(\frac{\partial f}{\partial a} \delta a)^2 + (\frac{\partial f}{\partial b} \delta b)^2 + ...}" />

## Örnekler
- Error: https://github.com/astrokod/Astro-Kod-Ders-26/blob/main/ornekler/acisal_uzaklik.ipynb
- Builder: https://github.com/astrokod/Astro-Kod-Ders-26/blob/main/ornekler/builder.ipynb
- Error: https://github.com/astrokod/Astro-Kod-Ders-26/blob/main/ornekler/value.ipynb
