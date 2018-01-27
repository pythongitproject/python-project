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
            '    <input type="text" class="form-control " name="bdparam" placeholder="key" size="35">\n' +
            '  </div>\n' +
            '\n' +
            '  <div class="form-group" >\n' +
            '  <input type="text" class="form-control" name="bdparam" placeholder="value" size="55">' +
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

    $("#testurl").blur(function () {
        var strs=$("#testurl").val().trim();
        if(strs!=''){
             $('#urlerror').text('');
        }else {
                $('#urlerror').text('接口名称不能为空!');
            }

    });

    $("#testname").blur(function () {
        var strs=$("#testname").val().trim();
        if(strs!=''){
             $('#tnerror').text('');
        }else {
            $('#tnerror').text('接口名称不能为空!');
        }

    });

    function urlComment() {
         //验证url网址
          var strs=$("#testurl").val().trim();
          if (strs ==''){
              $('#urlerror').text('URL地址不能为空!');
              return false
          }else {
              //判断URL地址的正则表达式为:http(s)?://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?
              //下面的代码中应用了转义字符"\"输出一个字符"/"
              var Expression=/http(s)?:\/\/([\w-]+\.)+[\w-]+(\/[\w- .\/?%&=]*)?/;
              var objExp=new RegExp(Expression);
              if(objExp.test(strs) != true){
                  $('#urlerror').text('URL格式有误，请重新输入!');
               return false;
              } else {
                  return true;
                }
          }

        }

    $('#test').click(function () {
         var testname = $("#testname").val().trim();
         var params = getbodyparams();
            if (testname!=''){
                 if(urlComment()){
                    var types = $("#select_value").val();
                    var testurl = $("#testurl").val();
                    $.ajax({
                        url:'/add_interface',
                        type:'post',
                        data : {
                        'testname':testname,
                        'testurl':testurl,
                        'types':types,
                            'params':getbodyparams(),
                        "_xsrf":$.cookie('_xsrf')
                    },
                        beforeSend:function () {
                             // 禁用按钮防止重复提交
                            $("#test").attr("disabled","disabled");
                            $('#my-modal-loading').modal('open');

                        },
                        success:function (data) {
                            var dd = JSON.parse(data);
                            if(dd.type==-1){
                                $("#test").removeAttr("disabled");
                                $('#my-modal-loading').modal('close');
                                $('#my-alert-timeout').modal('open');
                            }else {
                                $('#result').html(syntaxHighlight(dd.resbody));
                                $('#reheader').html(syntaxHighlight(dd.head));
                                $('#recode').html(dd.status_code);
                                $("#test").removeAttr("disabled");
                                $('#my-modal-loading').modal('close');
                            }
                        },
                       });
                }
            }else {
                $('#tnerror').text('接口名称不能为空!');
                return false;
            }

    });

    /*$("#ceshi").click(function () {
            var dic = ''
            var kk = $("input[name='bdparam']");/!*.each(function(){
              return $(this).val();
            }).get().join(", ")*!/
            for(var i = 0;i<kk.length;i++){
                if(i==0){
                    dic ='{' +'\"'+kk.eq(i).val().trim()+'\"' +':';
                }else {
                    if(i==1){
                    dic = dic +'\"'+ kk.eq(i).val().trim() +'\"'+',';
                    }else {
                        if(i%2==0){
                            dic = dic +'\"'+ kk.eq(i).val().trim()+'\"' +':';
                        }else {
                            if(i=kk.length-1){
                                dic = dic +'\"'+ kk.eq(i).val().trim()+'\"'+'}';
                            }else {
                                dic = dic +'\"'+ kk.eq(i).val().trim()+'\"' +',';
                            }

                        }
                    }
                }


            }
        console.log(dic);
        console.log(JSON.parse(dic));

    });*/


    function getbodyparams() {
            var dic = ''
            var kk = $("input[name='bdparam']");/*.each(function(){
              return $(this).val();
            }).get().join(", ")*/
            for(var i = 0;i<kk.length;i++){
                if(i==0){
                    dic ='{' +'\"'+kk.eq(i).val().trim()+'\"' +':';
                }else {
                    if(i==1){
                        if(i=kk.length-1){
                                dic = dic +'\"'+ kk.eq(i).val().trim()+'\"'+'}';
                            }else {
                                dic = dic +'\"'+ kk.eq(i).val().trim()+'\"' +',';
                            }
                    }else {
                        if(i%2==0){
                            dic = dic +'\"'+ kk.eq(i).val().trim()+'\"' +':';
                        }else {
                            if(i=kk.length-1){
                                dic = dic +'\"'+ kk.eq(i).val().trim()+'\"'+'}';
                            }else {
                                dic = dic +'\"'+ kk.eq(i).val().trim()+'\"' +',';
                            }

                        }
                    }
                }


            }
        //console.log(dic);
        //return JSON.stringify(dic);
        return dic;

    }
