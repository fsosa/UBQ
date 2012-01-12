$('#lab').live('pageinit',function(event){
	
	// Bind the pictures to the showing animation
	$("#pheno_img_hands").bind('click', function(){imageOnClick("#pheno_img_hands")});
	$("#pheno_img_horns").bind('click', function(){imageOnClick("#pheno_img_horns")});
	$("#pheno_img_mouth").bind('click', function(){imageOnClick("#pheno_img_mouth")});
	$("#pheno_img_tail").bind('click', function(){imageOnClick("#pheno_img_tail")});

	// Bind Hand Codons to CodonClick
	$('#amino_sequences_hands .ui-btn-text').css({margin: 0, padding: 0, left: '0%'});
	$('#codon_1_hands').bind('click', function() {CodonClick('#codon_1_hands')});
	$('#codon_2_hands').click(function() {CodonClick('#codon_2_hands')});
	$('#codon_3_hands').click(function() {CodonClick('#codon_3_hands')});
	$('#codon_4_hands').click(function() {CodonClick('#codon_4_hands')});
	$('#codon_5_hands').click(function() {CodonClick('#codon_5_hands')});
	$('#codon_6_hands').click(function() {CodonClick('#codon_6_hands')});
	$('#codon_7_hands').click(function() {CodonClick('#codon_7_hands')});
	$('#codon_8_hands').click(function() {CodonClick('#codon_8_hands')});
	$('#codon_9_hands').click(function() {CodonClick('#codon_9_hands')});

	// Bind Horn Codons to CodonClick
	$('#amino_sequences_horns .ui-btn-text').css({margin: 0, padding: 0, left: '0%'});
	$('#codon_1_horns').bind('click', function() {CodonClick('#codon_1_horns')});
	$('#codon_2_horns').click(function() {CodonClick('#codon_2_horns')});
	$('#codon_3_horns').click(function() {CodonClick('#codon_3_horns')});
	$('#codon_4_horns').click(function() {CodonClick('#codon_4_horns')});
	$('#codon_5_horns').click(function() {CodonClick('#codon_5_horns')});
	$('#codon_6_horns').click(function() {CodonClick('#codon_6_horns')});
	$('#codon_7_horns').click(function() {CodonClick('#codon_7_horns')});
	$('#codon_8_horns').click(function() {CodonClick('#codon_8_horns')});
	$('#codon_9_horns').click(function() {CodonClick('#codon_9_horns')});

	// Bind Mouth Codons to CodonClick
	$('#amino_sequences_mouth .ui-btn-text').css({margin: 0, padding: 0, left: '0%'});
	$('#codon_1_mouth').bind('click', function() {CodonClick('#codon_1_mouth')});
	$('#codon_2_mouth').click(function() {CodonClick('#codon_2_mouth')});
	$('#codon_3_mouth').click(function() {CodonClick('#codon_3_mouth')});
	$('#codon_4_mouth').click(function() {CodonClick('#codon_4_mouth')});
	$('#codon_5_mouth').click(function() {CodonClick('#codon_5_mouth')});
	$('#codon_6_mouth').click(function() {CodonClick('#codon_6_mouth')});
	$('#codon_7_mouth').click(function() {CodonClick('#codon_7_mouth')});
	$('#codon_8_mouth').click(function() {CodonClick('#codon_8_mouth')});
	$('#codon_9_mouth').click(function() {CodonClick('#codon_9_mouth')});

	// Bind Tail Codons to CodonClick
	$('#amino_sequences_tail .ui-btn-text').css({margin: 0, padding: 0, left: '0%'});
	$('#codon_1_tail').bind('click', function() {CodonClick('#codon_1_tail')});
	$('#codon_2_tail').click(function() {CodonClick('#codon_2_tail')});
	$('#codon_3_tail').click(function() {CodonClick('#codon_3_tail')});
	$('#codon_4_tail').click(function() {CodonClick('#codon_4_tail')});
	$('#codon_5_tail').click(function() {CodonClick('#codon_5_tail')});
	$('#codon_6_tail').click(function() {CodonClick('#codon_6_tail')});
	$('#codon_7_tail').click(function() {CodonClick('#codon_7_tail')});
	$('#codon_8_tail').click(function() {CodonClick('#codon_8_tail')});
	$('#codon_9_tail').click(function() {CodonClick('#codon_9_tail')});

	//bind fight button to FightClick
	$('#fight_button').click(FightClick);

	$('#dialog_close').click(function() {$('#fight_confirm').dialog('close');});

	$(function() {		
		
	// initialize scrollable
	$(".scrollable").scrollable({ vertical: true, circular: true});	
	
	});
    
    $(".pheno_list_item").click(PhenoListItemClick);
    
    if ($("#amino_sequences_hands").attr("title") == "Tap each nucleotide to change!")
	$("#amino_sequences_hands").tooltip({effect: 'fade', fadeOutSpeed: 10000});
})

function AdjustCodon(codon)
{
	short_sequence = $(codon).parent().text().replace(/\s+/gm,'');
	console.log(short_sequence);
	for (var i in genetic_code) {
		// if the sequence of 3 is in the dictionary
		if (i == short_sequence) {
			// Find the right text to update by using the number associated with codon id
			if (codon[7] <=3)
				$('#amino_select_1_' + current_phenotype).text(genetic_code[i]);
			else if (codon[7] <=6)
				$('#amino_select_2_' + current_phenotype).text(genetic_code[i]);
			else if (codon[7] <=9)
				$('#amino_select_3_' + current_phenotype).text(genetic_code[i]);
		}
	}
	sync(current_phenotype);
}

function CodonClick(codon) {
    if ($(codon).hasClass('locked') == true)
		return;
	// Grab the letter on the button
	current_codon = $(codon).text()[0];
	console.log(current_codon);
	// find index in dictionary
	current_index = codon_dict.indexOf(current_codon);
	console.log(current_index);
	// shift to the next letter in the sequence
	if (current_index == 3)
		$(codon).text(codon_dict[0]);
	else {
		$(codon).text(codon_dict[current_index + 1]);
	}
    
	AdjustCodon(codon);
}

