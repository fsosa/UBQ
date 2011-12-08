function FightClick() {
	$('#confirm_hands').attr('src', $('#pheno_img_hands').attr('src'));
	$('#confirm_horns').attr('src', $('#pheno_img_horns').attr('src'));
	$('#confirm_mouth').attr('src', $('#pheno_img_mouth').attr('src'));
	$('#confirm_tail').attr('src', $('#pheno_img_tail').attr('src'));

	for (var i in pheno_pics){
		if (pheno_pics[i] == $('#pheno_img_hands').attr('src')) {
			$('#confirm_hands_text').text(i);
		}
	}
	for (var i in pheno_pics){
		if (pheno_pics[i] == $('#pheno_img_horns').attr('src')) {
			$('#confirm_horns_text').text(i);
		}
	}
	for (var i in pheno_pics){
		if (pheno_pics[i] == $('#pheno_img_mouth').attr('src')) {
			$('#confirm_mouth_text').text(i);
		}
	}
	for (var i in pheno_pics){
		if (pheno_pics[i] == $('#pheno_img_tail').attr('src')) {
			$('#confirm_tail_text').text(i);
		}
	}
}
function amino_select_mouseover(event, select_id, type){
	var scroll = "#" + select_id;
	var api = $(scroll).data("scrollable")
	var index = api.getIndex();
	var amino_acid = api.getItems()[index].childNodes[1].childNodes[0].nodeValue;//options[amino_acid_seq];
	console.log(amino_acid);
	var sequence = amino_sequences[amino_acid];
	var amino_id = select_id
	if (amino_id == 'amino_select_1_' + current_phenotype) {
		$("#amino_1_" + current_phenotype +' >h1').text(sequence);
		sync(current_phenotype);
	}
	else if (amino_id == 'amino_select_2_' + current_phenotype) {
		$('#amino_2_' + current_phenotype + ' >h1').text(sequence);
		sync(current_phenotype);
	}
	else if (amino_id == 'amino_select_3_' + current_phenotype) {
		$('#amino_3_'+current_phenotype+ ' >h1').text(sequence);
		sync(current_phenotype);
	}
	//$('amino_' + amino_id > h1)
}


function sync(body_part) {
	// Boolean to determine whether or not a phenotype pic was found
	var changeBool = false;
	// All of the aminoacid sequences together
	var text = $('#amino_sequences_' + current_phenotype).text().replace(/\s+/gm,'');
	// Splice the text string into the separate ones, each representing the amino acid sequence
	var seq_1 = text.substring(0,3);
	var seq_2 = text.substring(3,6);
	var seq_3 = text.substring(6,9);
	var phenotype_seq = "";
	// If each sequence matches one of our amino_acids, add the abbreviation of the amino_acid to the phenotype_seq
	for (var i in amino_sequences) {
	if (amino_sequences[i] == seq_1)
	    phenotype_seq += (i.substring(0,3));
	}
	for (var i in amino_sequences) {
        if (amino_sequences[i] == seq_2)
             phenotype_seq += (i.substring(0,3));
	}
	for (var i in amino_sequences) {
        if (amino_sequences[i] == seq_3)
             phenotype_seq += (i.substring(0,3));
	}
	console.log(phenotype_seq);

	for (var i in pheno_pics) {
		//If the sequence matches a phenotype sequence that we have in a dictionary
		if (pheno_seq[i] == phenotype_seq){
			// Change and update the pic and text, ONLY if we are in the right body part
			var regexp = new RegExp(current_phenotype);
			// we check to see if we are in the right body part by looking at image filename (each one contains either "hands," "horns," etc.)
			if (regexp.test(pheno_pics[i]) != false) {
				UpdatePic(pheno_pics[i],i,body_part);


				// If we update pic, we have found a phenotype pic, so set bool to true
				changeBool = true;
			}
		}
	}

	// If we did not find a phenotype pic, we have to change picture to a normal one
	if (changeBool == false) {
		//Find the normal phenotype associated with the body part we are on
		var pattern = new RegExp("Normal " + current_phenotype.charAt(0).toUpperCase() + current_phenotype.substring(1));
		console.log(pattern.source);
		// Once we find it, call update pic with the normal one
		for (var i in pheno_pics) {
			if (pattern.test(i) == true)
				UpdatePic(pheno_pics[i], i, body_part);
		}
	}
	
}

function UpdatePic(phenotype, descr,body_part){
	if (body_part == 'hands') {
		$('#pheno_img_hands').attr('src', phenotype);
		console.log($('#current_Hands > img').attr('src'));
		$('#pheno_text_hands').text(descr);
	}
	else if (body_part == 'horns') {
		$('#pheno_img_horns').attr('src', phenotype);
		$('#pheno_text_horns').text(descr);
	}
	else if (body_part == 'mouth') {
		$('#pheno_img_mouth').attr('src', phenotype);
		$('#pheno_text_mouth').text(descr);
	}
	else if (body_part == 'tail') {
		$('#pheno_img_tail').attr('src', phenotype);
		$('#pheno_text_tail').text(descr);
	}
    //TODO Use for updating form values
    $('#fight_'+body_part).val(descr);
}

function imageOnClick(clicked) {
	var img_id = "#pheno_img_" + current_phenotype;
	var current_text = "#pheno_text_" + current_phenotype;
	var current_div = "#lab_" + current_phenotype;
	var new_text = "#pheno_text_" + clicked.substr(11);
	var show_div = "#lab_" + clicked.substr(11);
	
    console.log("img_id "+img_id)
    console.log("current_text "+current_text);
    console.log("current_div "+current_div);
    console.log("new_text "+new_text);
    console.log("show_div "+show_div);
    
	$(current_div).hide();
	$(show_div).show();
	$(current_text).text('');
	console.log(img_id);
	$(img_id).animate({
	width: '50',
	height: '50',
	opacity: 1,	
	}, {duration: 1000, queue: false});

	$(clicked).animate({
	width: '100',
	height: '100',
	opacity: 1,	
	}, {duration: 1000, queue: false});

	current_phenotype = clicked.substr(11);
    console.log("current_phenotype "+current_phenotype);
	for (var i in pheno_pics){
		if (pheno_pics[i] == $(clicked).attr('src'))
			$(new_text).text(i)
	}		
}

function PhenoListItemClick() {
	// Grab the phenotype name and corresponding sequence
    var pheno_name = $(this).data("phenotype");
    var aminoAcids = $(this).data("aminoacids");
	// split the sequence into the three amino acids
	var selected_amino1= aminoAcids.split("-")[0];
	var selected_amino2= aminoAcids.split("-")[1];
	var selected_amino3= aminoAcids.split("-")[2];

	// set the text on the genetic code screen
	$('#selected_phenotype').text(pheno_name);
	$('#selected_amino_1').text(selected_amino1);
	$('#selected_amino_2').text(selected_amino2);
	$('#selected_amino_3').text(selected_amino3);
	// color the backgrounds. Find the cells by class.
    //Set whole table to white
    for (var amino_acid in amino_abbreviations)
    {
        $('.' + amino_abbreviations[amino_acid]).css('background', '#FFFFFF');        
    }
    //Color select amino acids
	$('.' + selected_amino1).css('background', '#FF6666');
	$('.' + selected_amino2).css('background', '#FFFF66');
	$('.' + selected_amino3).css('background', '#99CCFF');
    $('#selected_image').attr('src', pheno_pics[pheno_name]);
}