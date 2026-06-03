// Поиск темы в кэше и установка светлой темы, есои её нет. Устанавливает тёмную тему если в кэше тёмная тема
if (!localStorage.getItem('current_theme')) {
    localStorage.setItem('current_theme', 'light');
}
else {
    const theme = localStorage.getItem('current_theme');
    if (theme == 'dark') {
        toggleThemeInstant()
    }
}

// Моментальная смена темы
function toggleThemeInstant() {
    var topline = document.getElementById("title");
    var themeSwitch = document.getElementById("themeSwitch");
    var blueline = document.getElementById("blueLine");
    var maincontent = document.getElementById("mainContent");
    var sopostavlenije = document.getElementById("sopostavlenije");
    var sunicon = document.getElementById("sunIcon");
    var moonicon = document.getElementById("moonIcon");
    var items = document.querySelectorAll("#markItem");

    topline.classList.toggle("dark-mode-borders");
    themeSwitch.classList.toggle("dark-mode-borders");
    moonicon.classList.toggle("dark-navigation");
    blueline.classList.toggle("dark-mode-purple");
    maincontent.classList.toggle("dark-mode-background");
    sopostavlenije.classList.toggle("dark-mode-borders");
    items.forEach((el) => {
        el.classList.toggle('dark-mode-background');
    });

    if (sunicon.style.display === "none") {
        sunicon.style.display = "block";
        moonicon.style.display = "none";
        localStorage.setItem('current_theme', 'light');
    } else {
        sunicon.style.display = "none";
        moonicon.style.display = "block";
        localStorage.setItem('current_theme', 'dark');
    }
}

// Плавный переход на другую тему для всех элементов
function toggleTheme() {
    const allElements = document.querySelectorAll('*');
    allElements.forEach(element => {
        element.style.transition = 'all 0.5s ease';
    });

    var topline = document.getElementById("title");
    var themeSwitch = document.getElementById("themeSwitch");
    var blueline = document.getElementById("blueLine");
    var maincontent = document.getElementById("mainContent");
    var sopostavlenije = document.getElementById("sopostavlenije");
    var sunicon = document.getElementById("sunIcon");
    var moonicon = document.getElementById("moonIcon");
    var items = document.querySelectorAll("#markItem");

    topline.classList.toggle("dark-mode-borders");
    themeSwitch.classList.toggle("dark-mode-borders");
    moonicon.classList.toggle("dark-navigation");
    blueline.classList.toggle("dark-mode-purple");
    maincontent.classList.toggle("dark-mode-background");
    sopostavlenije.classList.toggle("dark-mode-borders");
    items.forEach((el) => {
        el.classList.toggle('dark-mode-background');
    });

    if (sunicon.style.display === "none") {
        sunicon.style.display = "block";
        moonicon.style.display = "none";
        localStorage.setItem('current_theme', 'light');
    } else {
        sunicon.style.display = "none";
        moonicon.style.display = "block";
        localStorage.setItem('current_theme', 'dark');
    }

    setTimeout(() => {
        allElements.forEach(element => element.style.transition = '');
    }, 600);
}

const input = document.getElementById('mappingSearch');
let timeout;
input.addEventListener('input', () => {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    const q = input.value.trim().toLowerCase();
    document.querySelectorAll('.mark-item').forEach(el => {
      const text = el.innerText.toLowerCase();
      el.style.display = q === '' || text.includes(q) ? '' : 'none';
    });
  }, 150);
});

const select = document.getElementById('subjects');
select.addEventListener('change', () => {
  const val = select.value.toLowerCase();
  document.querySelectorAll('.mark-item').forEach(el => {
    if (val === 'all' || val === '') {
      el.style.display = '';
      return;
    }
    const subjectText = (el.querySelector('.subject')?.innerText || el.innerText).toLowerCase();
    el.style.display = subjectText.includes(val) ? '' : 'none';
  });
});