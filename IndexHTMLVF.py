<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Black Leather</title>
  <style>
    @font-face {
      font-family: 'Larida VF';
      src: url('https://victorortizzz.github.io/hostingVF/LaridaVF.woff') format('woff');
      font-weight: 100 900;
      font-display: swap;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      width: 100%;
      height: 100%;
      background: transparent;
      font-family: 'Larida VF', sans-serif;
    }

    #container {
      background: #000;
      color: #fff;
      width: 100%;
      height: calc(100% - 60px);
      border-radius: 1.5rem;
      display: flex;
      align-items: center;
      padding-left: 2rem;
      font-size: 4.8rem;
      letter-spacing: 0.03em;
    }

    #text-box {
      font-family: inherit;
      font-size: inherit;
      color: inherit;
      text-align: left;
      white-space: nowrap;
      outline: none;
      border: none;
      background: transparent;
      width: 100%;
      font-variation-settings: "wght" 900;
    }

    #slider-container {
      height: 60px;
      background: #111;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0 1rem;
    }

    input[type="range"] {
      width: 300px;
      accent-color: #fff;
    }

    label, #weight-value {
      color: #fff;
      font-family: sans-serif;
      margin: 0 0.5rem;
    }
  </style>
</head>
<body>
  <div id="container">
    <div id="text-box" contenteditable="true" spellcheck="false">Black Leather…</div>
  </div>

  <div id="slider-container">
    <label for="weight-slider">Peso:</label>
    <input type="range" id="weight-slider" min="100" max="900" step="1" value="900" />
    <span id="weight-value">900</span>
  </div>

  <script>
    const allowedChars = new Set(
      '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÄÉÍÓÔÕÖÚÜÝáäéíóôõöúüýĀāĄąĆćČčĎďĒēĖėĘęĚěĢģĪīĮįĶķĹĺĻļĽľŁłŃńŅņŇňŌōŐőŔŕŖŗŘřŚśŠšŤťŪūŰűŲųŹźŻżŽž¿?!¡!-—.,:;‘’“”„'
    );

    const textBox = document.getElementById('text-box');
    const weightSlider = document.getElementById('weight-slider');
    const weightValue = document.getElementById('weight-value');

    textBox.addEventListener('keydown', (e) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      if (e.key.length === 1 && !allowedChars.has(e.key)) {
        e.preventDefault();
      }
    });

    textBox.addEventListener('paste', (e) => {
      e.preventDefault();
      const text = (e.clipboardData || window.clipboardData).getData('text');
      const filtered = Array.from(text).filter(char => allowedChars.has(char)).join('');
      document.execCommand('insertText', false, filtered);
    });

    weightSlider.addEventListener('input', (e) => {
      const weight = e.target.value;
      textBox.style.fontVariationSettings = `"wght" ${weight}`;
      weightValue.textContent = weight;
    });
  </script>
</body>
</html>
