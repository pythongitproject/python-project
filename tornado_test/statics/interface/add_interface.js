    //新增raw参数
    $("#addraw").click(function () {
        var count = $('.bodyparam');
        if (count.length>0){
            $('#my-alert-raw').modal('open');
        }else {
            var normalcout =  $('#raw_count').val();
            if(normalcout==1){
                return false;
            }else {
                $(this).parent().append('<div class="addraw" style="margin-top: 10px">\n' +
            '<textarea class="form-control" rows="3" cols="108"></textarea>\n' +
             '  <input type="button"  class="btn btn-danger rmip" onclick="rmraw(this);" value="移除"/>'+
            '</div>');
             $('#raw_count').val(1);
            }
        }
    });
    
    //新增body参数
    $('#addbody').click(function () {
        var count = $(".addraw");
        if(count.length>0){
            //alert('请删除raw参数再重试');
            $('#my-alert').modal('open');
        }else {
            $(this).parent().append('<div class="form-inline bodyparam"  style="margin-top: 10px">\n' +
            '  <div class="form-group">\n' +
            '    <input type="text" class="form-control" placeholder="key" size="35">\n' +
            '  </div>\n' +
            '\n' +
            '  <div class="form-group" >\n' +
            '  <input type="text" class="form-control"  placeholder="value" size="55">' +
            '  <input type="button"  class="btn btn-danger rmip" onclick="rmbody(this);" value="移除"/>'+
            '  </div>\n' + '</div>');
        }



    });

    function rmbody (obj) {
        $(obj).parent().parent().remove();
    }

    function rmheader (obj) {
        $(obj).parent().parent().remove();
    }

    function rmraw (obj) {
        $(obj).parent().remove();
    }


    //新增header参数
    $('#addheader').click(function () {

        $(this).parent().append('<div class="form-inline" style="margin-top: 10px">\n' +
            '  <div class="form-group">\n' +
            '    <input type="text" class="form-control" placeholder="key" size="35">\n' +
            '  </div>\n' +
            '\n' +
            '  <div class="form-group" >\n' +
            '  <input type="text" class="form-control"  placeholder="value" size="55">' +
            '  <input type="button"  class="btn btn-danger" onclick="rmheader(this);" value="移除"/>'+
            '  </div>\n' + '</div>');
    });
    
    res='{\n' +
        ' "error": 0,\n' +
        ' "status": "success",\n' +
        ' "date": "2018-01-01"\n' +
        '}'

    $('#result').html(syntaxHighlight(res));

    //高亮显示代码块
    function syntaxHighlight(json) {
    if (typeof json != 'string') {
        json = JSON.stringify(json, undefined, 2);
    }
    json = json.replace(/&/g, '&').replace(/</g, '<').replace(/>/g, '>');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function(match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}


    $('#test').click(function () {
        var types = $("#select_value").val();
        var testname = $("#testname").val();
        var testurl = $("#testurl").val();
        var datas = {}

        console.log(types);
        $.ajax({
            url:'/test',
            type:types,
            data : datas,
            success:function () {
                alert('挺好');
            }
        });
    });