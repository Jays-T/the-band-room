/* Ready functions from Materialize */

$(document).ready(function () {
    /* to show/hide sidenav on smaller devices */
  $(".sidenav").sidenav();
   /* to stop the counter showing on each form input */
  $(".character-counter").hide();
});

/* Register form Password functions */

/* Toggle Show or Hide the password */
$("#register_show_password").click(function () {
  showPwd();
});

function showPwd() {
  let pwd = document.getElementById("user_key");
  if (pwd.type === "password") {
    pwd.type = "text";
  } else {
    pwd.type = "password";
  }
}

/* Compare both passwords on register page */

function comparePassword() {
  let passwordsMatch = false;
  let pwd1 = $("#user_key").val();
  let pwd2 = $("#user_key_check").val();
  if (pwd1 == pwd2) {
    $("#password_confirm").text(`Passwords match!`);
    $("#register_user_button").removeClass("disabled");
    passwordsMatch = true;
  } else {
    $("#password_confirm").text(`Passwords do not match!`);
    $("#register_user_button").addClass("disabled");
  }
}

/* Show delete room form */

$("#delete-room-btn").click(function () {
  $("#delete-room-form").removeClass("hide");
});
