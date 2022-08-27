const exp_btn = document.getElementById('user__exp__wrap');

function expAdditional(e) {
  if (e.target.id == 'empl_exp2') {
    const div = document.createElement('div');
    div.innerHTML = `<h2>Какую должность вы занимали?</h2>
                      <input type="text" class="user-text user__txt__exp__pos" value="" name="exp_position">

                      <h2>Как называлась организация?</h2>
                      <input type="text" class="user-text user__last__comp__name__exp" value="" name="org_name">

                      <h2 class="fw500 user-info-block-title">Обязанности</h2>
                      <div class="user__info__block__txt__area__wrapper">
                          <textarea name="responsibilities" id="job__resp"
                            class="user-info-block-txtarea user__response__exp"
                            placeholder="Расскажите обязанности и задачи которые вы выполняли на рабочем месте"></textarea>
                      </div>
                      <div class="user__time">
                          <h2>Начало работы</h2>
                          <select name="exp_start__month" id="user__exp__time__start__mon"
                            class="user__time__item user-select-bg user__time__start__mon__exp">
                            <option value="01">Январь</option>
                            <option value="02">Февраль</option>
                            <option selected value="03">Март</option>
                            <option value="04">Апрель</option>
                            <option value="05">Май</option>
                            <option value="06">Июнь</option>
                            <option value="07">Июль</option>
                            <option value="08">Август</option>
                            <option value="09">Сентябрь</option>
                            <option value="10">Октябрь</option>
                            <option value="11">Ноябрь</option>
                            <option value="12">Декабрь</option>
                          </select>

                          <div class="horizontal__row"></div>

                          <select name="exp_start__year" id="user__exp__time__start__year"
                            class="user__time__item user-select-bg user__time__start__year__exp">
                            <option value="2019">2019</option>
                            <option value="2018">2018</option>
                            <option value="2017">2017</option>
                            <option value="2016">2016</option>
                            <option value="2015">2015</option>
                            <option value="2014">2014</option>
                            <option value="2013">2013</option>
                            <option value="2012">2012</option>
                            <option value="2011">2011</option>
                            <option value="2010">2010</option>
                            <option value="2009">2009</option>
                            <option value="2008">2008</option>
                            <option value="2007">2007</option>
                            <option value="2006">2006</option>
                            <option value="2005">2005</option>
                            <option value="2004">2004</option>
                            <option value="2003">2003</option>
                            <option selected value="2002">2002</option>
                            <option value="2001">2001</option>
                            <option value="2000">2000</option>
                            <option value="1999">1999</option>
                            <option value="1998">1998</option>
                            <option value="1997">1997</option>
                            <option value="1996">1996</option>
                            <option value="1995">1995</option>
                            <option value="1994">1994</option>
                            <option value="1993">1993</option>
                            <option value="1992">1992</option>
                            <option value="1991">1991</option>
                            <option value="1990">1990</option>
                            <option value="1989">1989</option>
                            <option value="1988">1988</option>
                            <option value="1987">1987</option>
                            <option value="1986">1986</option>
                            <option value="1985">1985</option>
                            <option value="1984">1984</option>
                            <option value="1983">1983</option>
                            <option value="1982">1982</option>
                            <option value="1981">1981</option>
                            <option value="1980">1980</option>
                            <option value="1979">1979</option>
                            <option value="1978">1978</option>
                            <option value="1977">1977</option>
                            <option value="1976">1976</option>
                            <option value="1975">1975</option>
                          </select>
                      </div>

                      <div class="user__time">
                          <h2>Окончание работы</h2>
                          <select name="exp_end__month" id="user__exp__time__end__mon"
                            class="user__time__item user-select-bg user__time__end__mon__exp">
                            <option value="1">Январь</option>
                            <option value="2">Февраль</option>
                            <option selected value="3">Март</option>
                            <option value="4">Апрель</option>
                            <option value="5">Май</option>
                            <option value="6">Июнь</option>
                            <option value="7">Июль</option>
                            <option value="8">Август</option>
                            <option value="9">Сентябрь</option>
                            <option value="10">Октябрь</option>
                            <option value="11">Ноябрь</option>
                            <option value="12">Декабрь</option>
                          </select>

                          <div class="horizontal__row"></div>

                          <select name="exp_end__year" id="user__exp__time__end__year"
                            class="user__time__item user-select-bg user__time__end__year__exp">
                            <option value="2019">2019</option>
                            <option value="2018">2018</option>
                            <option value="2017">2017</option>
                            <option value="2016">2016</option>
                            <option value="2015">2015</option>
                            <option value="2014">2014</option>
                            <option value="2013">2013</option>
                            <option value="2012">2012</option>
                            <option value="2011">2011</option>
                            <option value="2010">2010</option>
                            <option value="2009">2009</option>
                            <option value="2008">2008</option>
                            <option value="2007">2007</option>
                            <option value="2006">2006</option>
                            <option value="2005">2005</option>
                            <option value="2004">2004</option>
                            <option value="2003">2003</option>
                            <option selected value="2002">2002</option>
                            <option value="2001">2001</option>
                            <option value="2000">2000</option>
                            <option value="1999">1999</option>
                            <option value="1998">1998</option>
                            <option value="1997">1997</option>
                            <option value="1996">1996</option>
                            <option value="1995">1995</option>
                            <option value="1994">1994</option>
                            <option value="1993">1993</option>
                            <option value="1992">1992</option>
                            <option value="1991">1991</option>
                            <option value="1990">1990</option>
                            <option value="1989">1989</option>
                            <option value="1988">1988</option>
                            <option value="1987">1987</option>
                            <option value="1986">1986</option>
                            <option value="1985">1985</option>
                            <option value="1984">1984</option>
                            <option value="1983">1983</option>
                            <option value="1982">1982</option>
                            <option value="1981">1981</option>
                            <option value="1980">1980</option>
                            <option value="1979">1979</option>
                            <option value="1978">1978</option>
                            <option value="1977">1977</option>
                            <option value="1976">1976</option>
                            <option value="1975">1975</option>
                          </select>

                          <div class="user__time__checkbox__wrapper">
                            <input type="checkbox" class="user__time__checkbox" id="user__t__chk" name="user__t__chk"
                                value="forpres">
                            <label for="user__t__chk" class="user__time__checkbox__label work_pres">Работаю по
                                настоящее
                                время</label>
                          </div>
                      </div>

               



                <div class="add__lang" id="addnew">
                    <span id="addnew">+</span>
                    <span id="addnew">Добавить опыт работы</span>
                </div>`
    document.getElementById("user__exp__wrap").appendChild(div);
    exp_btn.removeChild(document.getElementById('exp_btn_wrapper'));
    exp_btn.removeEventListener('click' , expAdditional);
  } else {
    
  }
}
exp_btn.addEventListener('click' , expAdditional);






let nameNum = 1;
document.getElementById("user__exp__btn__wrap").addEventListener("click", function (e) {
  const id = e.target.id;
  const div = document.createElement('div');
  if (id == "addnew") {
    div.innerHTML = `        
      <div>
        <h2 class="fw500">Опыт работы</h2>
        <h2>Какую должность вы занимали?</h2>
        <input type="text" class="user-text user__txt__exp__pos" value="" name="exp_position">

        <h2>Как называлсь организация?</h2>
        <input type="text" class="user-text user__last__comp__name__exp" value="" name="org_name">

        <h2 class="fw500 user-info-block-title">Обязанности</h2>
        <div class="user__info__block__txt__area__wrapper">
            <textarea name="responsibilities" id="job__resp"
              class="user-info-block-txtarea user__response__exp"
              placeholder="Расскажите обязанности и задачи которые вы выполняли на рабочем месте"></textarea>
        </div>
        <div class="user__time">
            <h2>Начало работы</h2>
            <select name="exp_start__month" id="user__exp__time__start__mon"
              class="user__time__item user-select-bg user__time__start__mon__exp">
              <option value="01">Январь</option>
              <option value="02">Февраль</option>
              <option selected value="03">Март</option>
              <option value="04">Апрель</option>
              <option value="05">Май</option>
              <option value="06">Июнь</option>
              <option value="07">Июль</option>
              <option value="08">Август</option>
              <option value="09">Сентябрь</option>
              <option value="10">Октябрь</option>
              <option value="11">Ноябрь</option>
              <option value="12">Декабрь</option>
            </select>

            <div class="horizontal__row"></div>

            <select name="exp_start__year" id="user__exp__time__start__year"
              class="user__time__item user-select-bg user__time__start__year__exp">
              <option value="2004">2004</option>
              <option value="2003">2003</option>
              <option selected value="2002">2002</option>
              <option value="2001">2001</option>
              <option value="2000">2000</option>
              <option value="1999">1999</option>
              <option value="1998">1998</option>
              <option value="1997">1997</option>
              <option value="1996">1996</option>
              <option value="1995">1995</option>
              <option value="1994">1994</option>
              <option value="1993">1993</option>
              <option value="1992">1992</option>
              <option value="1991">1991</option>
              <option value="1990">1990</option>
              <option value="1989">1989</option>
              <option value="1988">1988</option>
              <option value="1987">1987</option>
              <option value="1986">1986</option>
              <option value="1985">1985</option>
              <option value="1984">1984</option>
              <option value="1983">1983</option>
              <option value="1982">1982</option>
              <option value="1981">1981</option>
              <option value="1980">1980</option>
              <option value="1979">1979</option>
              <option value="1978">1978</option>
              <option value="1977">1977</option>
              <option value="1976">1976</option>
              <option value="1975">1975</option>
            </select>
        </div>

        <div class="user__time">
            <h2>Окончание работы</h2>
            <select name="exp_end__month" id="user__exp__time__end__mon"
              class="user__time__item user-select-bg user__time__end__mon__exp">
              <option value="1">Январь</option>
              <option value="2">Февраль</option>
              <option selected value="3">Март</option>
              <option value="4">Апрель</option>
              <option value="5">Май</option>
              <option value="6">Июнь</option>
              <option value="7">Июль</option>
              <option value="8">Август</option>
              <option value="9">Сентябрь</option>
              <option value="10">Октябрь</option>
              <option value="11">Ноябрь</option>
              <option value="12">Декабрь</option>
            </select>

            <div class="horizontal__row"></div>

            <select name="exp_end__year" id="user__exp__time__end__year"
              class="user__time__item user-select-bg user__time__end__year__exp">
              <option value="2004">2004</option>
              <option value="2003">2003</option>
              <option selected value="2002">2002</option>
              <option value="2001">2001</option>
              <option value="2000">2000</option>
              <option value="1999">1999</option>
              <option value="1998">1998</option>
              <option value="1997">1997</option>
              <option value="1996">1996</option>
              <option value="1995">1995</option>
              <option value="1994">1994</option>
              <option value="1993">1993</option>
              <option value="1992">1992</option>
              <option value="1991">1991</option>
              <option value="1990">1990</option>
              <option value="1989">1989</option>
              <option value="1988">1988</option>
              <option value="1987">1987</option>
              <option value="1986">1986</option>
              <option value="1985">1985</option>
              <option value="1984">1984</option>
              <option value="1983">1983</option>
              <option value="1982">1982</option>
              <option value="1981">1981</option>
              <option value="1980">1980</option>
              <option value="1979">1979</option>
              <option value="1978">1978</option>
              <option value="1977">1977</option>
              <option value="1976">1976</option>
              <option value="1975">1975</option>
            </select>

            <div class="user__time__checkbox__wrapper">
              <input type="checkbox" class="user__time__checkbox" id="user__t__chk"
                  name="user__t__chk" value="forpres">
              <label for="user__t__chk" class="user__time__checkbox__label work_pres">Работаю по
                  настоящее
                  время</label>
            </div>
        </div>
      </div>
    `
    document.getElementById("user__exp__wrap").appendChild(div);
  } else {
  }
});


document.getElementById("user__lang__btn__wrapper").addEventListener("click", function (e) {
  const id = e.target.id;
  const div = document.createElement('div');
  div.className = 'user__lang__item';
  if (id == "addnew") {
    div.innerHTML = `                           
    <div id="user__lang__wrap">
    <div class="user-info-block-subtitle">
       <div>Язык</div>
       <div>Уровень владения</div>
    </div>

    <div class="user-info-block__lang__item">
       <input type="text" class="user-info-block__lang__item__txt" name="language" id="user__lang"
          placeholder="Туркменский">
       <select name="lang__lev" id="lang__lev" class="user-info-block__lang__item__select">
          <option value="Базовый">Базовый</option>
          <option value="Продвинутый">Продвинутый</option>
          <option value="Свободно">Свободно</option>
          <option value="Совершенный">Совершенный</option>
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

document.getElementById("user__educ__btn__wrap").addEventListener("click", function (e) {
  const id = e.target.id;
  const div = document.createElement('div');
  div.className = 'user__educ__wrapper';
  if (id == "addnew") {
    div.innerHTML = `                           
    <h2 class="fw500">Образование</h2>
    <div class="user__exp__block" id="user__education__wrapper">
       <input required type="radio" id="educ1${nameNum}" value="среднее" name="edu_degrees${nameNum}">
       <label for="educ1${nameNum}" class="user__exp__item">среднее</label>
       <input required type="radio" id="educ2${nameNum}" value="средне-специальное" name="edu_degrees${nameNum}">
       <label for="educ2${nameNum}" class="user__exp__item">средне-специальное</label>
       <input required type="radio" id="educ3${nameNum}" value="неоконченное высшее" name="edu_degrees${nameNum}">
       <label for="educ3${nameNum}" class="user__exp__item">неоконченное высшее</label>
       <input required type="radio" id="educ4${nameNum}" value="высшее" name="edu_degrees${nameNum}">
       <label for="educ4${nameNum}" class="user__exp__item">высшее</label>
       <input required type="radio" id="educ6${nameNum}" value="магистр" name="edu_degrees${nameNum}">
       <label for="educ6${nameNum}" class="user__exp__item">магистр</label>
       <input required type="radio" id="educ7${nameNum}" value="кандидат наук" name="edu_degrees${nameNum}">
       <label for="educ7${nameNum}" class="user__exp__item">кандидат наук</label>
       <input required type="radio" id="educ8${nameNum}" value="доктор наук" name="edu_degrees${nameNum}">
       <label for="educ8${nameNum}" class="user__exp__item">доктор наук</label>
    </div>


    <h2>Учебное заведение</h2>
    <input type="text" class="user-text user__edu__instance" value="" name="establishment"
       id="user__edu__inst">




    <h2>Факультет</h2>
    <input type="text" class="user-text" value="" name="faculty" id="user__faculty">



    <h2>Специализация</h2>
    <input type="text" class="user-text user__specialize" value="" name="specialization"
       id="user__spec">



    <div class="user__time">
       <div class="user__titles">
          <h2>Год начала </h2>
          <h2>Год окончания</h2>
       </div>
       <div class="user__time__inner">
          <select name="start_year_edu" id="user__time__educ__start__year"
             class="user__time__item user-select-bg user__time__start__year__educ">
             <option value="2004">2004</option>
             <option value="2003">2003</option>
             <option selected value="2002">2002</option>
             <option value="2001">2001</option>
             <option value="2000">2000</option>
             <option value="1999">1999</option>
             <option value="1998">1998</option>
             <option value="1997">1997</option>
             <option value="1996">1996</option>
             <option value="1995">1995</option>
             <option value="1994">1994</option>
             <option value="1993">1993</option>
             <option value="1992">1992</option>
             <option value="1991">1991</option>
             <option value="1990">1990</option>
             <option value="1989">1989</option>
             <option value="1988">1988</option>
             <option value="1987">1987</option>
             <option value="1986">1986</option>
             <option value="1985">1985</option>
             <option value="1984">1984</option>
             <option value="1983">1983</option>
             <option value="1982">1982</option>
             <option value="1981">1981</option>
             <option value="1980">1980</option>
             <option value="1979">1979</option>
             <option value="1978">1978</option>
             <option value="1977">1977</option>
             <option value="1976">1976</option>
             <option value="1975">1975</option>
          </select>

          <div class="horizontal__row"></div>


          <select name="end_year_edu" id="user__time__educ__end__year"
             class="user__time__item user-select-bg user__time__start__year__educ">
             <option value="2004">2004</option>
             <option value="2003">2003</option>
             <option selected value="2002">2002</option>
             <option value="2001">2001</option>
             <option value="2000">2000</option>
             <option value="1999">1999</option>
             <option value="1998">1998</option>
             <option value="1997">1997</option>
             <option value="1996">1996</option>
             <option value="1995">1995</option>
             <option value="1994">1994</option>
             <option value="1993">1993</option>
             <option value="1992">1992</option>
             <option value="1991">1991</option>
             <option value="1990">1990</option>
             <option value="1989">1989</option>
             <option value="1988">1988</option>
             <option value="1987">1987</option>
             <option value="1986">1986</option>
             <option value="1985">1985</option>
             <option value="1984">1984</option>
             <option value="1983">1983</option>
             <option value="1982">1982</option>
             <option value="1981">1981</option>
             <option value="1980">1980</option>
             <option value="1979">1979</option>
             <option value="1978">1978</option>
             <option value="1977">1977</option>
             <option value="1976">1976</option>
             <option value="1975">1975</option>
          </select>
       </div>
    </div>
`
    document.getElementById("user__educ__container").appendChild(div);
    console.log(div);
    nameNum++;
    console.log(nameNum);
    return nameNum;
  } else {
  }
});

document.getElementById("user__progs__btn__wrapper").addEventListener("click", function (e) {
  const id = e.target.id;
  const div = document.createElement('div');
  if (id == "addnew") {
    div.innerHTML = `                           
    <input type="text" class="user-text user__progs" value="" name="program" id="user__prog">`
    document.getElementById("user__progs__wrapper").appendChild(div);
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

