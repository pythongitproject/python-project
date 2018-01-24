
    function isPoneAvailable(str) {
          var myreg=/^[1][3,4,5,,6,7,8,9][0-9]{9}$/;
          if (!myreg.test(str)) {
              return true;
          } else {
              return false;
          }
      }
    //刷新验证码
    function Changecode() {
            $("#getcode").attr("src","/check_code?flag="+Math.random());
    }
    $("#sb").on("click",function () {
        var flag = true;
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
                        $("#msg").text('登录密码不能为空哦');
                    }else {
                        if ($("#code").val().trim()==''){
                            flag=false;
                            $("#msg").text('验证码不能为空哦');
                        }else {
                             if(flag){
                            $.post("/login",
                            {"telno":$("#telno").val().trim(),"password":$("#pwd").val().trim(),"code":$("#code").val().trim()},
                            function (callback) {
                               var data = callback;
                               var ret_dict = JSON.parse(data);
                               console.log(ret_dict)
                               if(ret_dict.status){
                                   window.location.href = "/index";
                               }else {
                                   var id = ret_dict.typeid;
                                   switch (id){
                                       case -1 :
                                           $("#telno").val("");
                                           $("#pwd").val("");
                                           $("#code").val("");
                                           Changecode();
                                           $("#msg").text(ret_dict.msg);
                                           break;
                                       case -2 :
                                           Changecode();
                                           $("#code").val("");
                                            $("#msg").text(ret_dict.msg);
                                           break;
                                       case -3 :
                                           layer.msg('该用户不存在哦', {
                                              time: 0 //不自动关闭
                                              ,btn: ['点击注册', '再试下']
                                              ,yes: function(index){
                                                layer.close(index);
                                                window.location.href = "/signup";
                                              }
                                            });
                                           Changecode();
                                           $("#telno").val("");
                                           $("#pwd").val("");
                                           $("#code").val("");
                                           break;
                                       default:
                                           alert('网络君闹情绪了,请重试！')
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


