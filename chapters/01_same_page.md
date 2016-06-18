% Same Page
# Let's make sure we're on the same page #

Let's start off with a small example program.

Java:

~~~
public static void main(String... args) {
    System.out.println("Hello World!");
    return;
}
~~~

And racket:

~~~
#lang racket
;; Finds Racket sources in all subdirs
(for ([path (in-directory)]
      #:when (regexp-match? #rx"[.]rkt$" path))
  (printf "source file: ~a\n" path))
~~~

End.
