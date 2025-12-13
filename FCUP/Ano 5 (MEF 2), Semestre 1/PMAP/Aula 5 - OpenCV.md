- Para importar e ver uma imagem (respetivamente) usamos: `cv.imread()` e `imshow()` assim
```python
img_grey_cat = cv.imread("./Data/grey_cat-png", cv2.IMREAD_GRAYSCALE)
cv2_imshow(image_grey_cat)
```
em a parte `IMREAD_GRAYSCALE` a imagem fica a cores
- OpenCV normalmente usa BGR invés de RGB. Isto quer dizer que ao importar uma imagem normal, o OpenCV vai inverter as cores porque assume BGR. Existem funções para inverter

- Ao processar, cortar ou fazer qualquer coisa numa ROI, temos isso também vai alterar a **imagem original** portanto temos que fazer uma cópia