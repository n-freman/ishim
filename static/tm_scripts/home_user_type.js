const textArea = document.getElementById('u_t_txt');
const employee = document.getElementById('employee');
const hirer = document.getElementById('hirer');

employee.addEventListener('click' , (e) => {
   e.preventDefault();

   if (document.getElementById('employee_btn').classList.contains('disappear')) {
      document.getElementById('employee_btn').classList.add('intro__desc__item__btn');
      document.getElementById('employee_btn').classList.remove('disappear');
      document.getElementById('hirer_btn').classList.remove('intro__desc__item__btn');
      document.getElementById('hirer_btn').classList.add('disappear');
      textArea.innerHTML = 'Tiz iş tapmak üçin çözgütdir '
   }
})

hirer.addEventListener('click' , (e) => {
   e.preventDefault();

   if (document.getElementById('hirer_btn').classList.contains('disappear')) {
      document.getElementById('hirer_btn').classList.add('intro__desc__item__btn');
      document.getElementById('hirer_btn').classList.remove('disappear');
      document.getElementById('employee_btn').classList.remove('intro__desc__item__btn');
      document.getElementById('employee_btn').classList.add('disappear');
      textArea.innerHTML = 'Işim-da boş iş wezipeleri ýerleşdiriň we biz bilen size laýyk işgärleri tapyň. Ishim - täze işe alyş usuly.'
   }
})