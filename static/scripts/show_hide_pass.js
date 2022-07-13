document.getElementById('form__id').addEventListener('click' , e => {
   if (e.target.id == 'eye__btn') {
      if (e.target.getAttribute('src') == 'http://127.0.0.1:8000/static/images/close__eye.svg') {
         e.target.src = 'http://127.0.0.1:8000/static/images/open__eye.svg';
         e.target.previousElementSibling.type = 'text';
      }else{
         e.target.src = 'http://127.0.0.1:8000/static/images/close__eye.svg';
         e.target.previousElementSibling.type = 'password';
      }

   }
})
