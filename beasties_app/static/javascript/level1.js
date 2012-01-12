$(window).load(function(event){
//Adjust initial amino acid sequences
    $("#amino_select_1_hands").data("scrollable").seekTo(0, 1000);
	$("#amino_select_2_hands").data("scrollable").seekTo(1, 1000);
	$("#amino_select_3_hands").data("scrollable").seekTo(2, 1000);
    
    $("#amino_select_1_horns").data("scrollable").seekTo(5, 1000);
	$("#amino_select_2_horns").data("scrollable").seekTo(6, 1000);
	$("#amino_select_3_horns").data("scrollable").seekTo(7, 1000);
    
    $("#amino_select_1_mouth").data("scrollable").seekTo(8, 1000);
	$("#amino_select_2_mouth").data("scrollable").seekTo(9, 1000);
	$("#amino_select_3_mouth").data("scrollable").seekTo(10, 1000);
    
    $("#amino_select_1_tail").data("scrollable").seekTo(2, 1000);
	$("#amino_select_2_tail").data("scrollable").seekTo(3, 1000);
	$("#amino_select_3_tail").data("scrollable").seekTo(4, 1000);

    //Only display hand options
    $("#lab_horns").hide();
	$("#lab_mouth").hide();
	$("#lab_tail").hide();	    
});

$('#lab').live('pageinit',function(event){

	$("#pheno_img_hands").bind('click', function(){imageOnClick("#pheno_img_hands")});
	$("#pheno_img_horns").bind('click', function(){imageOnClick("#pheno_img_horns")});
	$("#pheno_img_mouth").bind('click', function(){imageOnClick("#pheno_img_mouth")});
	$("#pheno_img_tail").bind('click', function(){imageOnClick("#pheno_img_tail")});

	$("#amino_select_1_hands").bind('onSeek', function() {amino_select_mouseover('','amino_select_1_hands', 'prev')});
	$("#amino_select_2_hands").bind('onSeek', function() {amino_select_mouseover('','amino_select_2_hands', 'prev')});
	$("#amino_select_3_hands").bind('onSeek', function() {amino_select_mouseover('','amino_select_3_hands', 'prev')});

	$("#amino_select_1_horns").bind('onSeek', function() {amino_select_mouseover('','amino_select_1_horns', 'prev')});
	$("#amino_select_2_horns").bind('onSeek', function() {amino_select_mouseover('','amino_select_2_horns', 'prev')});
	$("#amino_select_3_horns").bind('onSeek', function() {amino_select_mouseover('','amino_select_3_horns', 'prev')});

	$("#amino_select_1_mouth").bind('onSeek', function() {amino_select_mouseover('','amino_select_1_mouth', 'prev')});
	$("#amino_select_2_mouth").bind('onSeek', function() {amino_select_mouseover('','amino_select_2_mouth', 'prev')});
	$("#amino_select_3_mouth").bind('onSeek', function() {amino_select_mouseover('','amino_select_3_mouth', 'prev')});

	$("#amino_select_1_tail").bind('onSeek', function() {amino_select_mouseover('','amino_select_1_tail', 'prev')});
	$("#amino_select_2_tail").bind('onSeek', function() {amino_select_mouseover('','amino_select_2_tail', 'prev')});
	$("#amino_select_3_tail").bind('onSeek', function() {amino_select_mouseover('','amino_select_3_tail', 'prev')});

    //TODO Add fight screen confirm
    //Confirm fight
    $('#fight_button').click(FightClick);

    //Cancel fight
    $('#dialog_close').click(function() {$('#fight_confirm').dialog('close');});
	$(function() {		
		
	// initialize scrollable with mousewheel support
	$(".scrollable").scrollable({ vertical: true, circular: true});	
	
	});
	
	// initialize tooltip
    if ($("#amino_select_2_hands").attr("title") == "Swipe with your finger to change amino acid!")
	$("#amino_select_2_hands").tooltip({effect: 'fade', fadeOutSpeed: 10000});
    
    $(".pheno_list_item").click(PhenoListItemClick);

})