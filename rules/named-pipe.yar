rule Detect_Named_Pipe
{
    meta:
        author = "hail0hyrda"
        description = "Detect is a named pipe is being created"

    strings:
        $sc1 = "mkfifo" // searching for syscall string of named pipes
        $sc2 = "mknod" // can also be used for named pipes
        $w = "write" //  additionals
        $r = "read" // additionals

    condition:
        ( $sc1 or $sc2 ) or ( $w or $r ) //just give it all
}
