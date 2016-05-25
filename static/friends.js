// Where do we want to use Ajax requests?

$(document).ready(function(){
  getFriends()

  $('form.create').submit(function(e){
    // CREATE A FRIEND
    // Prevented automatic page refresh
    e.preventDefault()
    // Gather form information into a string
    var formInfo = $(this).serialize();
    createFriend(formInfo)
  })

  $('div.friends').on('click', 'button.delete', function(){
    // Grab user ID:
    var friendID = $(this).attr('data-id')
    deleteFriend(friendID)
  })

  $('div.friends').on('click', 'a', function(e){
    e.preventDefault()
    var friendID = $(this).attr('data-id')
    showFriend(friendID)
  })

})

function createFriend(newFriend){
  $.ajax({
    url: '/friends',
    method: 'POST',
    data: newFriend,
    success: function(){
      $('form.create').trigger('reset')
      getFriends()
    }
  })
}
function getFriends(){
  $.ajax({
    url: '/get_friends',
    method: 'GET',
    success: function( friendsTemplate ) {
      $('.friend').html('')
      $('.friends').html(friendsTemplate)
    }
  })
}

function deleteFriend(id){
  $.ajax({
    url: `/friends/${id}/delete`,
    method: 'POST',
    success: getFriends
  })
}

function showFriend(){
  $.ajax({
    url: `/friends/${id}`,
    success: function( friendTemplate ){
      $('.friends').html('')
      $('.friend').html(friendTemplate)
    }
  })
}


// 1. Form submission => create a friend

// 2. Updating a friend
// 3. Deleting a friend
// 4. Showing a friend
