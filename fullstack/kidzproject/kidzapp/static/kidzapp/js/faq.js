// $(document).ready(function () {
//     $(".accordion-title").click(function (e) {
//       var accordionitem = $(this).attr("data-tab");
//       $("#" + accordionitem)
//         .slideToggle()
//         .parent()
//         .siblings()
//         .find(".accordion-content")
//         .slideUp();

//       $(this).toggleClass("active-title");
//       $("#" + accordionitem)
//         .parent()
//         .siblings()
//         .find(".accordion-title")
//         .removeClass("active-title");

//       $("i.fa-chevron-down", this).toggleClass("chevron-top");
//       $("#" + accordionitem)
//         .parent()
//         .siblings()
//         .find(".accordion-title i.fa-chevron-down")
//         .removeClass("chevron-top");
//     });
//   });
// select all accordion items
const accItems = document.querySelectorAll(".accordion__item");

// add a click event for all items
accItems.forEach((acc) => acc.addEventListener("click", toggleAcc));

function toggleAcc() {
  // remove active class from all items exept the current item (this)
  accItems.forEach((item) => item != this ? item.classList.remove("accordion__item--active") : null
  );

  // toggle active class on current item
  if (this.classList != "accordion__item--active") {
    this.classList.toggle("accordion__item--active");
  }
}
