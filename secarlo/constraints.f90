subroutine ray_casting(n, edges, x, y, inside)
  implicit none
  integer, parameter :: dp = kind(1.d0)
  integer :: i, n
  real(dp) :: edges(n, 2, 2)
  real(dp) :: x, y
  real(dp) :: a(2), b(2), m_edge, m_point
  logical :: inside
  real(dp), parameter :: eps  = 0.00001
  
  !f2py intent(in) edges, x, y 
  !f2py depend(n) edges
  !f2py intent(out) inside

  ! No need to count if we just initialize with false
  inside = .false.

  ! edge is an array with ((x1, y1), (x2, y2))
  
  do i = 1, n

     ! a should be the lowest point
     if (edges(i, 1, 2) > edges(i, 2, 2)) then
          a = edges(i, 2, :)
          b = edges(i, 1, :)
     else
          a = edges(i, 1, :)
          b = edges(i, 2, :)
     end if

       ! if we are on a vertex perturb the point
     if ((y == a(2)) .or. (y == b(2))) then
        y = y + eps
     end if
        
     ! First cases for no intersection
     if ((y > b(2)) .or. (y < a(2)) .or. (x > max(a(1), b(1)))) then
        continue
     elseif (x < min(a(1), b(1))) then
        inside = .not. inside
     end if

     ! edge check
     if (abs(a(1) - b(1)) > tiny(a(1))) then
        m_edge = (b(2) - a(2)) / (b(1) - a(1))
     else
        m_edge = huge(m_edge)
     end if

     ! point check
     if (abs(a(1) - x) > tiny(a(1))) then
        m_point = (y - a(2)) / (x - a(1))
     else
        m_point = huge(m_point)
     end if

     ! last condition
     if (m_point >= m_edge) then
        inside = .not. inside
     end if
     
     
  end do
  
  
  
end subroutine ray_casting

subroutine ray_casting_array(n, m, edges, x, y, inside)
  implicit none
  integer, parameter :: dp = kind(1.d0)
  integer :: i, j, n, m
  real(dp) :: edges(n, 2, 2)
  real(dp) :: x(m), y(m)
  real(dp) :: a(2), b(2), m_edge, m_point
  logical :: inside(m)
  real(dp), parameter :: eps  = 0.00001
  
  !f2py intent(in) edges, x, y 
  !f2py depend(n) edges
  !f2py depend(m) x, y, inside
  !f2py intent(out) inside

  do j = 1, m
  ! No need to count if we just initialize with false
  inside(j) = .false.

  ! edge is an array with ((x1, y1), (x2, y2))
  
  do i = 1, n

     ! a should be the lowest point
     if (edges(i, 1, 2) > edges(i, 2, 2)) then
          a = edges(i, 2, :)
          b = edges(i, 1, :)
     else
          a = edges(i, 1, :)
          b = edges(i, 2, :)
     end if

       ! if we are on a vertex perturb the point
     if ((y(j) == a(2)) .or. (y(j) == b(2))) then
        y(j) = y(j) + eps
     end if
        
     ! First cases for no intersection
     if ((y(j) > b(2)) .or. (y(j) < a(2)) .or. (x(j) > max(a(1), b(1)))) then
        continue
     elseif (x(j) < min(a(1), b(1))) then
        inside(j) = .not. inside(j)
     end if

     ! edge check
     if (abs(a(1) - b(1)) > tiny(a(1))) then
        m_edge = (b(2) - a(2)) / (b(1) - a(1))
     else
        m_edge = huge(m_edge)
     end if

     ! point check
     if (abs(a(1) - x(j)) > tiny(a(1))) then
        m_point = (y(j) - a(2)) / (x(j) - a(1))
     else
        m_point = huge(m_point)
     end if

     ! last condition
     if (m_point >= m_edge) then
        inside(j) = .not. inside(j)
     end if
     
     
  end do
  
end do
  
end subroutine ray_casting_array
