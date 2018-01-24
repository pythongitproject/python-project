
        function isPoneAvailable(str) {
          var myreg=/^[1][3,4,5,,6,7,8,9][0-9]{9}$/;
          if (!myreg.test(str)) {
              return true;
          } else {
              return false;
          }
       }

    $("#sb").on("click",function () {
        var flag = true;
        if($("#uname").val().trim()=='' ){
            flag = false;
            $("#msg").text('用户名不能为空哦');
        }else {
            if($("#telno").val().trim()==''){
                flag=false;
                $("#msg").text('手机号码不能为空哦');
            }else {
                if ($("#telno").val().trim().length<11 || isPoneAvailable($("#telno").val().trim())){
                    flag=false;
                    $("#msg").text('请输入11位的手机号码哦');
                }else {
                    if($("#pwd").val().trim()==''){
                flag=false;
                $("#msg").text('请输入登录密码');
                }else {
                    if(flag){
                        $.post("/signup",
                        {"username":$("#uname").val().trim(),"password":$("#pwd").val().trim(),"telno":$("#telno").val().trim()},
                        function (callback) {
                           var data = callback;
                           var ret_dict = JSON.parse(data);
                           console.log(ret_dict)
                           if(ret_dict.status){
                               $("#msg").text("");
                               layer.msg('注册成功，请点击确定前往登录页', {
                                  time: 0 //不自动关闭
                                  ,btn: ['确定', '不想去了']
                                  ,yes: function(index){
                                    layer.close(index);
                                    window.location.href = "/login";
                                  }
                                });

                           }else {
                               var id = ret_dict.typeid;
                               switch (id){
                                   case -1 :
                                       $("#uname").val("");
                                       $("#pwd").val();
                                       $("#telno").val();
                                       $("#msg").text(ret_dict.msg);
                                       break;
                                   case -2 :
                                       layer.msg('该用户已注册哦', {
                                              time: 0 //不自动关闭
                                              ,btn: ['点击前往登录', '再想想']
                                              ,yes: function(index){
                                                layer.close(index);
                                                window.location.href = "/login";
                                              }
                                            });
                                       $("#pwd").val("");
                                       break;
                                   default:
                                       $("#uname").val("");
                                       $("#pwd").val("");
                                       $("#telno").val("");
                                       $("#msg").text(ret_dict.msg);
                                       break;
                               }
                           }
                        });

                    }
                }
                }
            }
        }

    });
