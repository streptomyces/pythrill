use 5.14.0;
use List::Util qw(any);

print(@ARGV);
print("\n");

my @pairs;

my ($fn1, $fn2);
for $fn1 (@ARGV) {
  for $fn2 (@ARGV) {
    my $p1 = $fn1 . "--" . $fn2;
    my $p2 = $fn2 . "--" . $fn1;
    if(any { $_ eq $p1 } @pairs) {
      next;
    }
    elsif(any { $_ eq $p2 } @pairs) {
      next;
    }
    elsif($fn2 eq $fn1) { print "same file\n"; next; }
    else { push(@pairs, $p1, $p2); fcomp($fn1, $fn2) }
  }
}


sub fcomp {
  my $fn1 = shift(@_);
  my $fn2 = shift(@_);

  open(FH1, "<", $fn1);
  open(FH2, "<", $fn2);

  while(my $line1 = readline(FH1)) {
    chomp($line1);
    my $lc2 = 0;
    seek(FH2, 0, 0);
    while(my $line2 = readline(FH2)) {
      chomp($line2);
      # print("======= $line2 $line1\n");
      $lc2 += 1;
      if($line2 eq $line1) {
        print("$lc2\t$fn1\t$line1\t$fn2\t$line2\n");
        last;
      }
    }
  }
  close(FH2);
  close(FH1);
}

print(join("\n", @pairs));
print("\n");

