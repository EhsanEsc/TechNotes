// Metafunction : a class with zero+ template parametrs and zero+ return types and values
// returning value :static constexpr int value = 10;
// returning type : using type = T;

template <auto X, auto Y>
struct Sum {
  static constexpr auto value = X + Y;
};

template <auto X>
inline constexpr auto ValueIdentity_v =
  ValueIdentity<X>::value;

template <typename T>
using TypeIdentity_t = typename TypeIdentity::type;

// we should add typename if compiler does not know the type of ::type

// std::integral_constant
// a very usefull
// (), ()(), value_type, ::value

template <class T, T v>
struct integral_constant {
  static constexpr T value = v;
  //...
}

template <bool B>
using bool_constant = integral_constant<bool, B>;
using true_type = bool_constant<true>;
using false_type = bool_constant<false>;

// Do not specialize standard type traits
// Be very careful when using incomplete types

// SPECIALIZATION
// is_void

template <typename T>
struct is_void : std::false_type{};

template<>
struct is_void<void> : std::true_type{};

static_assert(is_void<void>{});
static_assert(not is_void<int>{});

// T and CV T yield same result (const volatile)

// Transformation Trait
// remove_const -> remove any top level const qualifier

// templaet<> : full specialization
// templaet<..> : partial specialization
// Compiler : which one is has the best match(most specialization)?

// Conditional
template<bool Cond, typename T, typename F>
struct conditional : TypeIdentity<T> {};

template<typename T, typename F>
struct conditional<false, T, F> : TypeIdentity<F> {};

// For any given type T, exactly one of the primary type categories(14)
// shall yield true_type

// type in pack

template <typename T>
struct is_array : std::false_type {};

template <typename T, std::size_t N>
struct is_array<T[N]> : std::true_type {};

template <typename T>
struct is_array<T[]> : std::true_type {};

// In specialization u must have exact number of template parametrs

// member pointer
struct Bar {};
using AZ = int Bar::*;

namespace detail {
  std::true_type is_nullptr(std::nullptr_t);
  std::false_type is_nullptr(...);
}

template<typename T>
using is_null_pointr = decltype(detail::is_nullptr(std::declval<t>()));
// decltype : pretend to call function but dont! return the type u could returns

// SFINAE : Subsitiotion failure is not an error
template <typename T>
std::true_type can_have_pointer_to_member(int T::*);
template <typename T>
std::false_type can_have_pointer_to_member(...);

template <typename T>
  can_have_member_ptr =
    decltype(can_have_pointer_to_member<t>(nullptr));
  
