function loadScript()
{    
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = "https://code.jquery.com/jquery-3.3.1.slim.min.js";
    head.appendChild(script);
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = "https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js";
    head.appendChild(script);
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = "https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js";
    head.appendChild(script);
}

loadScript();