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
    var topline = document.getElementById("title")
    var theme = document.getElementById("themeSwitch")
    var blueline = document.getElementById("blueLine")
    var maincontent = document.getElementById("mainContent")
    var sopostavlenije = document.getElementById("sopostavlenije")
    var sunicon = document.getElementById("sunIcon");
    var moonicon = document.getElementById("moonIcon");
    var item = document.querySelectorAll("#markItem");
    var login_form = document.getElementById("loginForm")
    var login_input = document.getElementById("inputLogin")
    var login_field = document.getElementById("login")
    var password_field = document.getElementById("password")
    

    topline.classList.toggle("dark-mode-borders");
    theme.classList.toggle("dark-mode-borders");
    moonicon.classList.toggle("dark-navigation")
    blueline.classList.toggle("dark-mode-purple");
    maincontent.classList.toggle("dark-mode-background");
    login_form.classList.toggle("dark-mode-background");
    sopostavlenije.classList.toggle("dark-mode-borders");
    login_input.classList.toggle("evil");
    login_field.classList.toggle("dark-mode-borders");
    password_field.classList.toggle("dark-mode-borders");

    item.forEach((el) => {
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

    var topline = document.getElementById("title")
    var theme = document.getElementById("themeSwitch")
    var blueline = document.getElementById("blueLine")
    var maincontent = document.getElementById("mainContent")
    var sopostavlenije = document.getElementById("sopostavlenije")
    var sunicon = document.getElementById("sunIcon");
    var moonicon = document.getElementById("moonIcon");
    var item = document.querySelectorAll("#markItem");
    var login_form = document.getElementById("loginForm")
    var login_input = document.getElementById("inputLogin")
    var login_field = document.getElementById("login")
    var password_field = document.getElementById("password")
    

    topline.classList.toggle("dark-mode-borders");
    theme.classList.toggle("dark-mode-borders");
    moonicon.classList.toggle("dark-navigation");
    blueline.classList.toggle("dark-mode-purple");
    maincontent.classList.toggle("dark-mode-background");
    login_form.classList.toggle("dark-mode-background");
    sopostavlenije.classList.toggle("dark-mode-borders");
    login_input.classList.toggle("evil");
    login_field.classList.toggle("dark-mode-borders");
    password_field.classList.toggle("dark-mode-borders");

    item.forEach((el) => {
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