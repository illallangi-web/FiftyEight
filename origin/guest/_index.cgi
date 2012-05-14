#!/usr/bin/perl 

$FORM{'node'} = "index";

#Initialise - print content type, header and get values passed.
@pairs = split(/&/, $ENV{'QUERY_STRING'}); 
foreach $pair (@pairs) { 
	($name, $value) = split(/=/, $pair); 
	$value =~ tr/+/ /; 
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg; 
	$FORM{$name} = $value; 
} 

print "Content-type: text/html\n\n";

print "<html>";

if ($FORM{'add'} EQ "yes") {

	print "<!-- $FORM{'name'} -->\n";
	print "<!-- $FORM{'email'} -->\n";
	print "<!-- $FORM{'web'} -->\n";;
	print "<!-- $FORM{'message'} -->\n";
	if (open(MESSAGES, ">>index.txt")) {
		print MESSAGES "<table width=100% cellspacing=0 cellpadding=5>";
		print MESSAGES "<tr height=4 bgcolor=white><td></td><td></td><td></td></tr>";
		print MESSAGES "<tr><td width=10%><b>$FORM{'name'}</b><br>$FORM{'email'}<br>";
		print MESSAGES "<a href=\"$FORM{'web'}\">$FORM{'web'}</a></td>\n";
		print MESSAGES "<td width=1 bgcolor=white></td>";
		print MESSAGES "<td><pre>$FORM{'message'}</pre></td></tr>";
		print MESSAGES "<tr height=4 bgcolor=white><td></td><td></td><td></td></tr>";
		print MESSAGES "</table>\n";

	    close(MESSAGES);
	}
;

}


open(DATA,"index.txt");
        @index = <DATA>;
close (DATA);
chomp(@index);

print "
 <head>
  <title>FiftyEight</title>
 </head>
<script>
function WM_on(id){
    document.getElementById(id).style.display = 'block';
}
function WM_off(id){
    document.getElementById(id).style.display = 'none';
}
</script>
 <body bgcolor=black text=white style=\"padding: 0; border: 0; indent: 0\">
  <table width=100% border=0>
   <tr>
    <td rowspan=4></td>
    <td width=600 align=center valign=middle>
     <a href=\"../\" onmouseover=\"WM_on('div1'); return false\" onmouseout=\"WM_off('div1'); return false\"><img
id=\"mainpic\" src=\"../fiftyeight.png\" width=324 height=38\" border=0></a>
    </td>
    <td rowspan=4></td>
   </tr>
   <tr>
    <td align=center valign=middle>
     <img src=\"title.png\">
    </td>
   </tr>
   <tr>
    <td align=center valign=middle>
      <form method=\"GET\" action=\"index.cgi\">
      <input type=\"hidden\" name=\"add\" value=\"yes\">
      Your Name: <input type=\"text\" name=\"name\" size=\"20\" value=\"\"><br>
      Your Email: <input type=\"text\" name=\"email\" size=\"20\" value=\"\"><br>
      Your WebSite: <input type=\"text\" name=\"web\" size=\"20\" value=\"http://\"><br>
      Your Message:<br>
      <textarea rows=\"10\" name=\"message\" cols=\"40\"></textarea><br>
      <input type=\"submit\" value=\"Submit\">
     </form>
    </td>
   </tr>

   <tr>
    <td align=center valign=middle>";

print "@index";

print "    </td>
   </tr>
  </table>
 </body>
</html>";
