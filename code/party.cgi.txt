#!/usr/bin/perl 

#Initialise - print content type, header and get values passed.
@pairs = split(/&/, $ENV{'QUERY_STRING'});
foreach $pair (@pairs) {
        ($name, $value) = split(/=/, $pair);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        $FORM{$name} = $value;
}


print "Content-type: text/html\n\n";

open(DATA,"$FORM{'col'}.hed");
        @index = <DATA>;
close (DATA);

foreach $line (@index)
{
	print $line;
}

print "<table width=100% border=0 cellpadding=0 cellspacing=0>\n\n";

@index = `ls ./$FORM{'col'}/ | grep jpg\$`;
chomp(@index);

$align = "1";
$olign = "0";

print "<tr height=5><td colspan=3 bgcolor=black></td></tr>";

foreach $line (@index)
{
	($image, $file) = split(/&/, $line);

$image =~ s/%actv%/$actv/g;
$image =~ s/%ill%/$ill/g;

	$tlign = $align;
	$align = $olign;
	$olign = $tlign;


	print "<tr><td>\n";
	if ($align eq "1") {
		print "<a href=$image.jpg>";
		print "<img src=$FORM{'col'}/$image align=$align border=0 height=100>";
		print "</a>";
	}

	print "</td><td align=center
width=100%><h2>$text</h2></td><td>";

	if ($align eq "0") {
		print "<a href=$image.jpg>";
		print "<img src=$FORM{'col'}/$image align=$align border=0 height=100>";
		print "</a>";
	}
	print "</td></tr>\n";
print "<tr height=5><td colspan=3 bgcolor=black></td></tr>";

}

print "\n</table>\n";
print "</body>\n";
print "</html>\n";
