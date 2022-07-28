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
      textArea.innerHTML = 'Все что вам нужно для быстрого поиска работы'
   }
})

hirer.addEventListener('click' , (e) => {
   e.preventDefault();

   if (document.getElementById('hirer_btn').classList.contains('disappear')) {
      document.getElementById('hirer_btn').classList.add('intro__desc__item__btn');
      document.getElementById('hirer_btn').classList.remove('disappear');
      document.getElementById('employee_btn').classList.remove('intro__desc__item__btn');
      document.getElementById('employee_btn').classList.add('disappear');
      textArea.innerHTML = 'Размещайте вакансии на ishim.com и находите у нас подходящих сотрудников. Ishim-  это новая модель найма работников.'
   }
})