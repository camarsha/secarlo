subroutine transport_element (n, m, samples, x_in, coeff, power, x_out)
  ! Transform input array into output array using the
  ! cosy maps
  
  implicit none
  
  integer, parameter :: dp = kind(1.d0)
  integer :: i, j, k, l, n, m, samples
  real(dp) :: coeff(n, m), power(n, m, n)
  real(dp) :: x_in(samples, n)
  real(dp) :: x_out(samples, n)
  real(dp) :: power_temp(samples)
  !f2py intent(in) x_in, coeff, power 
  !f2py depend(samples, n) x_in, x_out
  !f2py depend(n, m) coeff, power
  !f2py intent(out) x_out

  
  x_out = 0.0

  
  
  ! Perform the multiplication of the arrays
  do i = 1, n
     ! Loop over the coefficients
     do j = 1, m
        ! stop the loop once we get to the padding zeros
        if (abs(coeff(i, j)) .le. 1.d-80) then
           exit
        else
           ! Loop over the powers
           power_temp = 1.0
           ! loop over the samples
           do l = 1, samples
              do k = 1, n
                 power_temp(l) = power_temp(l) * x_in(l, k)**power(i, j, k)
              end do
              ! final output 
              x_out(l, i) = x_out(l, i) + power_temp(l) * coeff(i, j)
           end do
        end if
     end do
  end do


  
end subroutine transport_element

! subroutine transport_system (n, m, total, x_in, coeff, power, x_out)

!   implicit none
!   integer, parameter :: dp = kind(1.d0)
!   integer :: i, j, n, m, total
!   real(dp) :: coeff(total, n, m), power(total, n, m, n)
!   real(dp) :: x_in(n)
!   real(dp) :: x_out(total, n)
!   !f2py intent(in) x_in, coeff, power 
!   !f2py depend(n) x_in
!   !f2py depend(total, n) x_out
!   !f2py depend(total, n, m) coeff, power
!   !f2py intent(out) x_out


!   ! this sucks for some reason that I don't understand :(
!   ! Might just be the effect of the padding zeros
  
!   do j = 1, n
!      x_out(1, j) = x_in(j)
!   end do
  
!   do i = 1, total
!      call transport_element(n, m, x_out(i, :), coeff(i, :, :), power(i, :, :, :), x_out(i+1, :))
!   end do

! end subroutine transport_system
