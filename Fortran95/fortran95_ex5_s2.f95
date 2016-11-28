! Script 2

do n = 1, 500
	if (mod(n, 3) = 2) then
		if (mod(n, 5) = 3) then
			if (mod(n, 7) = 2) then
				print "(i3 ,1x\)", n
			endif
		endif
	endif
enddo

end