

jump(){

if [ -z "$1" ] ; then

	echo "empty"

else

if [ -z "$2" ] ; then

	dirr=$(find ~/ -iname *$1* 2>&1  |grep -v -i "find: "| wc -l)
	dir=$(find ~/ -iname *$1* 2>&1  |grep -v -i "find: "| fzy)
	#cd $dir
	echo $dirr
else
if [ $2 =="-x" ] ; then

	dirr=$(find / -iname *$1* 2>&1  |grep -v -i "find: "| wc -l)
        dir=$(find / -iname *$1* 2>&1  |grep -v -i "find: "| fzy)
        echo $dirr


	if [ -d "$dir" ] ; then

        cd "$dir"


	else

#Navigate to a file


	if [ -f "$dir" ]; then
		dir=$(dirname "$dir")
		cd "$dir"
	fi
	fi

fi
fi
fi		 }
