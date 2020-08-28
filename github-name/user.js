// ==UserScript==
// @name         Github-Name
// @namespace    https://github.com/crclz
// @version      0.2
// @description  在issue显示预先设置的真实姓名
// @author       crclz
// @match        https://github.com/buaa21/summer2020/issues/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    const uRefText =
        `黄坚	havesomecolo
    宋友	songyou21
    杨晴虹	iceryang
    路新喜	laneseal
    陈泓瑞	crclz
    李鑫	SeventhGX
    邢湧喆	orixing
    卓佩妍	PineZhuo
    邢智涣	Roycent
    胡鹏飞	IAmParasite
    王立芃	Lighten-w
    石泽宏	Zehong3351
    张梓航	songoku1994`

    const teachers = { '黄坚': '', '宋友': '', '杨晴虹': '', '路新喜': '' }

    var nameRef = {}

    for (var line of uRefText.split('\n')) {
        var [name, username] = line.trim().split(/\s+/);
        nameRef[username] = name
    }

    setInterval(() => {
        var elist = document.getElementsByClassName('author');
        for (var e of elist) {
            var username = e.innerHTML;
            if (username in nameRef) {
                var name = nameRef[username]
                if (name in teachers) {
                    e.innerHTML += `<font color="red"> ${name} (教师) </font>`
                } else {
                    e.innerHTML += `<font color="blue"> ${name} (助教) </font>`
                }
            }
        }
    }, 1000)

})();