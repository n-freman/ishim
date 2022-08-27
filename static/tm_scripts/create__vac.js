let nameNum = 1;
document.getElementById("user__lang__btn__wrapper").addEventListener("click", function (e) {
   const id = e.target.id;
   const div = document.createElement('div');
   div.className = 'user__lang__item';
   if (id == "addnew") {
     div.innerHTML = `                           
      <div class="user-info-block-subtitle">
        <div>Dil</div>
        <div>bilim derejesi</div>
      </div>

      <div class="user-info-block__lang__item">
        <input type="text" class="user-info-block__lang__item__txt" name="language" id="user__lang"
        placeholder="Türkmen dili">
        <select name="level" id="lang__lev" class="user-info-block__lang__item__select">
        <option value="esasy">esasy</option>
        <option value="gepleşik">gepleşik</option>
        <option value="ýokary dereje">ýokary dereje</option>
        <option value="tehniki taýdan">tehniki taýdan</option>
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
