var submit = function () {
    openpgp.init();
    var publickey = openpgp.read_publicKey($("#publickey").html());
    var plaintext = ""
    plaintext += "From: " + $("#from").val() + "\n"
    plaintext += "Subject: " + $("#subject").val() + "\n\n"
    plaintext += $("#msg").val();

    var ciphertext = openpgp.write_encrypted_message(publickey, plaintext);

    $('<input>').attr({
            type: 'hidden',
            name: 'encrypted',
            value: ciphertext
    }).appendTo('#msgform');
};
$('#msgform').submit(submit);
