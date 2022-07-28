const deleteElem = document.getElementById('delete__btn');
deleteElem.addEventListener('click' ,  () =>{
   const delete_block = document.createElement('div');
   delete_block.className = 'delete__content__content';
   delete_block.innerHTML = `
         <h1 class="delete__title">
            Ishim sahypada akaundyňyzy dikeltmesiz pozmagyny tassyklaýarsyňyzmy? Ähli şahsy maglumatlaryňyz, saýlalanlaryňyz we mahabatlaryňyz hemişelik pozular.
         </h1>
         <div class="delete__btns__wrapper">
            <div class="red__btn" id="sure"><a href="/delete-me/" data-method="delete">Pozmak</a></div>
            <div class="grey__btn" id="not_sure">Ýatyrmak</div>
         </div>`
   document.getElementById('delete__wrap').appendChild(delete_block);
   Next(delete_block);
});
 function Next(delete_block) {
   const not_sure = document.getElementById('not_sure');
   not_sure.addEventListener('click' , (e) => {
      e.preventDefault();
      document.getElementById('delete__wrap').removeChild(delete_block);
   });
};

