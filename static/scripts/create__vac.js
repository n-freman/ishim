let nameNum = 1;
document.getElementById("user__lang__btn__wrapper").addEventListener("click", function (e) {
   const id = e.target.id;
   const div = document.createElement('div');
   div.className = 'user__lang__item';
   if (id == "addnew") {
     div.innerHTML = `                           
      <div class="user-info-block-subtitle">
        <div>Язык</div>
        <div>Уровень владения</div>
      </div>

      <div class="user-info-block__lang__item">
        <input type="text" class="user-info-block__lang__item__txt" name="language" id="user__lang"
        placeholder="Туркменский">
        <select name="level" id="lang__lev" class="user-info-block__lang__item__select">
          <option value="Базовый">Базовый</option>
          <option value="Продвинутый">Продвинутый</option>
          <option value="Говорю свободно">Говорю свободно</option>
          <option value=">В совершенстве">В совершенстве</option>
          <option value="Профильный">Профильный</option>
        </select>
      </div>`
     document.getElementById("user__lang__wrap").appendChild(div);
     console.log(div);
     nameNum++;
     console.log(nameNum);
     return nameNum;
   } else {
   }
 });


const selectIndustry = document.getElementById('user__industry');
selectIndustry.addEventListener('change' , (e) => {
  let index =  selectIndustry.selectedIndex;
  console.log(index);
  if(index == 14) {
    document.getElementById('industry__wrapper').removeChild(selectIndustry);
     const div = document.createElement('div');
     div.className = 'user-inp-blok';
     div.innerHTML = `<input required type="text" class="user-text" value="" placeholder="Другое" name="sphere" id="anotherIndustryId">`
     document.getElementById('industry__wrapper').appendChild(div);
  }
});
