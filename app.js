// app.js
function showScreen(id) {
  const target = document.getElementById(id);

  if (!target) {
    console.error(`showScreen: no screen found with id "${id}"`);
    return;
  }

  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  target.classList.add('active');

  document.body.classList.remove('birak-bg', 'kambarang-bg', 'makuru-bg');
  if (id === 'birak') document.body.classList.add('birak-bg');
  if (id === 'kambarang') document.body.classList.add('kambarang-bg');
  if (id === 'makuru') document.body.classList.add('makuru-bg');
}